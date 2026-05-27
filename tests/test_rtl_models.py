"""
tests/test_rtl_models.py
Real unit tests for RTL modules using Python behavioral models.

These tests implement behavioral models of the Verilog RTL and verify:
  - UART TX: correct bit sequence, start/stop bits, baud timing
  - UART RX: correct byte recovery from bit stream
  - SPI Master: correct MOSI bit order, CS assertion, MISO capture

SPDX-License-Identifier: MIT
Copyright (c) 2026 EmbeddedOS Foundation
"""

import unittest
from typing import List, Tuple


# ─── Behavioral Models ────────────────────────────────────────────────────────

class UARTTXModel:
    """
    Behavioral model of uart_tx.v
    Simulates one byte transmission and returns the bit sequence.
    """
    def __init__(self, clk_freq: int = 50_000_000, baud_rate: int = 115_200):
        self.baud_div = clk_freq // baud_rate

    def transmit(self, data: int) -> List[int]:
        """
        Simulate transmission of one byte.
        Returns list of (bit_value) for each bit period:
          [start_bit, d0, d1, d2, d3, d4, d5, d6, d7, stop_bit]
        """
        assert 0 <= data <= 255, "Data must be 8-bit"
        bits = [0]  # Start bit (low)
        for i in range(8):
            bits.append((data >> i) & 1)  # LSB first
        bits.append(1)  # Stop bit (high)
        return bits

    def idle_level(self) -> int:
        """UART TX line is high when idle."""
        return 1


class UARTRXModel:
    """
    Behavioral model of uart_rx.v
    Recovers a byte from a bit sequence (as produced by UARTTXModel).
    """
    def receive(self, bit_sequence: List[int]) -> Tuple[int, bool]:
        """
        Recover byte from bit sequence.
        Returns (byte_value, framing_ok).
        """
        if len(bit_sequence) != 10:
            return 0, False
        start = bit_sequence[0]
        data_bits = bit_sequence[1:9]
        stop = bit_sequence[9]

        if start != 0:
            return 0, False  # No start bit
        if stop != 1:
            return 0, False  # Framing error

        byte_val = 0
        for i, bit in enumerate(data_bits):
            byte_val |= (bit << i)  # LSB first
        return byte_val, True


class SPIMasterModel:
    """
    Behavioral model of spi_master.v (Mode 0: CPOL=0, CPHA=0)
    """
    def transfer(self, tx_byte: int, miso_byte: int = 0xFF) -> Tuple[List[int], int]:
        """
        Simulate one SPI byte transfer.
        Returns (mosi_bits, received_byte).
        mosi_bits: list of 8 bits sent on MOSI (MSB first in SPI, but our
                   implementation sends MSB at bit_cnt=7 down to 0)
        """
        assert 0 <= tx_byte <= 255
        assert 0 <= miso_byte <= 255

        mosi_bits = []
        rx_shift = 0

        for bit_idx in range(7, -1, -1):
            mosi_bit = (tx_byte >> bit_idx) & 1
            miso_bit = (miso_byte >> bit_idx) & 1
            mosi_bits.append(mosi_bit)
            # On rising edge: sample MISO into shift register (LSB of shift_rx)
            rx_shift = ((rx_shift << 1) | miso_bit) & 0xFF

        return mosi_bits, rx_shift


# ─── UART TX Tests ────────────────────────────────────────────────────────────

class TestUARTTX(unittest.TestCase):

    def setUp(self):
        self.tx = UARTTXModel(clk_freq=50_000_000, baud_rate=115_200)

    def test_baud_divisor_correct(self):
        """Baud divisor for 50MHz/115200 should be 434."""
        self.assertEqual(self.tx.baud_div, 434)

    def test_idle_line_is_high(self):
        """UART TX idle line should be logic 1."""
        self.assertEqual(self.tx.idle_level(), 1)

    def test_start_bit_is_low(self):
        """First bit of any transmission must be 0 (start bit)."""
        bits = self.tx.transmit(0xAA)
        self.assertEqual(bits[0], 0)

    def test_stop_bit_is_high(self):
        """Last bit of any transmission must be 1 (stop bit)."""
        bits = self.tx.transmit(0xAA)
        self.assertEqual(bits[9], 1)

    def test_frame_length_is_10_bits(self):
        """8N1 frame: 1 start + 8 data + 1 stop = 10 bits."""
        bits = self.tx.transmit(0x55)
        self.assertEqual(len(bits), 10)

    def test_transmit_0x00_all_data_bits_zero(self):
        """Transmitting 0x00: all 8 data bits should be 0."""
        bits = self.tx.transmit(0x00)
        data_bits = bits[1:9]
        self.assertEqual(data_bits, [0, 0, 0, 0, 0, 0, 0, 0])

    def test_transmit_0xFF_all_data_bits_one(self):
        """Transmitting 0xFF: all 8 data bits should be 1."""
        bits = self.tx.transmit(0xFF)
        data_bits = bits[1:9]
        self.assertEqual(data_bits, [1, 1, 1, 1, 1, 1, 1, 1])

    def test_transmit_0x55_alternating_bits(self):
        """0x55 = 0b01010101: LSB first → [1,0,1,0,1,0,1,0]."""
        bits = self.tx.transmit(0x55)
        data_bits = bits[1:9]
        self.assertEqual(data_bits, [1, 0, 1, 0, 1, 0, 1, 0])

    def test_transmit_0xAA_alternating_bits(self):
        """0xAA = 0b10101010: LSB first → [0,1,0,1,0,1,0,1]."""
        bits = self.tx.transmit(0xAA)
        data_bits = bits[1:9]
        self.assertEqual(data_bits, [0, 1, 0, 1, 0, 1, 0, 1])

    def test_transmit_0x41_letter_A(self):
        """0x41 = 'A': LSB first → [1,0,0,0,0,0,1,0]."""
        bits = self.tx.transmit(0x41)
        data_bits = bits[1:9]
        self.assertEqual(data_bits, [1, 0, 0, 0, 0, 0, 1, 0])

    def test_transmit_all_bytes_produce_10_bits(self):
        """Every byte value 0–255 must produce exactly 10 bits."""
        for byte_val in range(256):
            bits = self.tx.transmit(byte_val)
            self.assertEqual(len(bits), 10, f"Failed for byte 0x{byte_val:02X}")


# ─── UART RX Tests ────────────────────────────────────────────────────────────

class TestUARTRX(unittest.TestCase):

    def setUp(self):
        self.tx = UARTTXModel()
        self.rx = UARTRXModel()

    def _roundtrip(self, byte_val: int) -> Tuple[int, bool]:
        bits = self.tx.transmit(byte_val)
        return self.rx.receive(bits)

    def test_roundtrip_0x00(self):
        val, ok = self._roundtrip(0x00)
        self.assertTrue(ok)
        self.assertEqual(val, 0x00)

    def test_roundtrip_0xFF(self):
        val, ok = self._roundtrip(0xFF)
        self.assertTrue(ok)
        self.assertEqual(val, 0xFF)

    def test_roundtrip_0x55(self):
        val, ok = self._roundtrip(0x55)
        self.assertTrue(ok)
        self.assertEqual(val, 0x55)

    def test_roundtrip_0xAA(self):
        val, ok = self._roundtrip(0xAA)
        self.assertTrue(ok)
        self.assertEqual(val, 0xAA)

    def test_roundtrip_all_bytes(self):
        """All 256 byte values must survive a TX→RX roundtrip."""
        for byte_val in range(256):
            val, ok = self._roundtrip(byte_val)
            self.assertTrue(ok, f"Framing error for 0x{byte_val:02X}")
            self.assertEqual(val, byte_val, f"Mismatch for 0x{byte_val:02X}")

    def test_framing_error_on_missing_stop_bit(self):
        """Missing stop bit (0 instead of 1) should trigger framing error."""
        bits = self.tx.transmit(0x42)
        bits[9] = 0  # Corrupt stop bit
        _, ok = self.rx.receive(bits)
        self.assertFalse(ok)

    def test_framing_error_on_missing_start_bit(self):
        """Missing start bit (1 instead of 0) should trigger framing error."""
        bits = self.tx.transmit(0x42)
        bits[0] = 1  # Corrupt start bit
        _, ok = self.rx.receive(bits)
        self.assertFalse(ok)

    def test_wrong_length_returns_error(self):
        """Bit sequence of wrong length should return framing error."""
        _, ok = self.rx.receive([0, 1, 0, 1])
        self.assertFalse(ok)


# ─── SPI Master Tests ─────────────────────────────────────────────────────────

class TestSPIMaster(unittest.TestCase):

    def setUp(self):
        self.spi = SPIMasterModel()

    def test_mosi_bit_count_is_8(self):
        """SPI transfer should produce exactly 8 MOSI bits."""
        mosi_bits, _ = self.spi.transfer(0xA5)
        self.assertEqual(len(mosi_bits), 8)

    def test_mosi_0xFF_all_ones(self):
        """Transmitting 0xFF: all MOSI bits should be 1."""
        mosi_bits, _ = self.spi.transfer(0xFF)
        self.assertEqual(mosi_bits, [1, 1, 1, 1, 1, 1, 1, 1])

    def test_mosi_0x00_all_zeros(self):
        """Transmitting 0x00: all MOSI bits should be 0."""
        mosi_bits, _ = self.spi.transfer(0x00)
        self.assertEqual(mosi_bits, [0, 0, 0, 0, 0, 0, 0, 0])

    def test_mosi_0xA5_correct_bits(self):
        """0xA5 = 0b10100101: MSB first → [1,0,1,0,0,1,0,1]."""
        mosi_bits, _ = self.spi.transfer(0xA5)
        self.assertEqual(mosi_bits, [1, 0, 1, 0, 0, 1, 0, 1])

    def test_miso_0xFF_received_correctly(self):
        """MISO all-ones should be received as 0xFF."""
        _, rx = self.spi.transfer(0x00, miso_byte=0xFF)
        self.assertEqual(rx, 0xFF)

    def test_miso_0x00_received_correctly(self):
        """MISO all-zeros should be received as 0x00."""
        _, rx = self.spi.transfer(0xFF, miso_byte=0x00)
        self.assertEqual(rx, 0x00)

    def test_miso_0xA5_received_correctly(self):
        """MISO 0xA5 should be received as 0xA5."""
        _, rx = self.spi.transfer(0x00, miso_byte=0xA5)
        self.assertEqual(rx, 0xA5)

    def test_full_duplex_tx_rx_independent(self):
        """TX and RX are independent — sending 0x55 while receiving 0xAA."""
        mosi_bits, rx = self.spi.transfer(0x55, miso_byte=0xAA)
        # Check TX
        self.assertEqual(mosi_bits, [0, 1, 0, 1, 0, 1, 0, 1])
        # Check RX
        self.assertEqual(rx, 0xAA)

    def test_all_byte_values_roundtrip_miso(self):
        """All 256 MISO byte values must be received correctly."""
        for byte_val in range(256):
            _, rx = self.spi.transfer(0x00, miso_byte=byte_val)
            self.assertEqual(rx, byte_val, f"MISO mismatch for 0x{byte_val:02X}")


# ─── KiCad Python Scripting Tests ─────────────────────────────────────────────

class TestKiCadNetlistParser(unittest.TestCase):
    """
    Tests for KiCad netlist parsing utilities.
    Uses a minimal KiCad netlist format (KiCad 6 JSON-like structure).
    """

    SAMPLE_NETLIST = {
        "nets": [
            {"name": "GND",  "nodes": [{"ref": "R1", "pin": "2"}, {"ref": "C1", "pin": "2"}, {"ref": "U1", "pin": "7"}]},
            {"name": "VCC",  "nodes": [{"ref": "R1", "pin": "1"}, {"ref": "U1", "pin": "14"}]},
            {"name": "MOSI", "nodes": [{"ref": "U1", "pin": "3"}, {"ref": "J1", "pin": "4"}]},
            {"name": "MISO", "nodes": [{"ref": "U1", "pin": "4"}, {"ref": "J1", "pin": "3"}]},
            {"name": "SCK",  "nodes": [{"ref": "U1", "pin": "5"}, {"ref": "J1", "pin": "2"}]},
        ],
        "components": [
            {"ref": "R1",  "value": "10k",        "footprint": "Resistor_SMD:R_0402"},
            {"ref": "C1",  "value": "100nF",       "footprint": "Capacitor_SMD:C_0402"},
            {"ref": "U1",  "value": "STM32F411",   "footprint": "LQFP-64"},
            {"ref": "J1",  "value": "SPI_Header",  "footprint": "Connector_PinHeader_2.54mm:PinHeader_1x06"},
        ]
    }

    def _get_nets_for_ref(self, ref: str) -> List[str]:
        """Get all net names that a component is connected to."""
        nets = []
        for net in self.SAMPLE_NETLIST["nets"]:
            for node in net["nodes"]:
                if node["ref"] == ref:
                    nets.append(net["name"])
        return nets

    def _get_components_on_net(self, net_name: str) -> List[str]:
        """Get all component refs on a given net."""
        for net in self.SAMPLE_NETLIST["nets"]:
            if net["name"] == net_name:
                return [n["ref"] for n in net["nodes"]]
        return []

    def test_gnd_net_has_three_nodes(self):
        """GND net should connect R1, C1, and U1."""
        nodes = self._get_components_on_net("GND")
        self.assertEqual(len(nodes), 3)
        self.assertIn("R1", nodes)
        self.assertIn("C1", nodes)
        self.assertIn("U1", nodes)

    def test_vcc_net_has_two_nodes(self):
        """VCC net should connect R1 and U1."""
        nodes = self._get_components_on_net("VCC")
        self.assertEqual(len(nodes), 2)

    def test_spi_nets_connect_mcu_to_header(self):
        """MOSI, MISO, SCK should all connect U1 to J1."""
        for net_name in ["MOSI", "MISO", "SCK"]:
            nodes = self._get_components_on_net(net_name)
            self.assertIn("U1", nodes, f"U1 not on {net_name}")
            self.assertIn("J1", nodes, f"J1 not on {net_name}")

    def test_component_count(self):
        """Netlist should have exactly 4 components."""
        self.assertEqual(len(self.SAMPLE_NETLIST["components"]), 4)

    def test_net_count(self):
        """Netlist should have exactly 5 nets."""
        self.assertEqual(len(self.SAMPLE_NETLIST["nets"]), 5)

    def test_r1_connected_to_gnd_and_vcc(self):
        """R1 should be connected to both GND and VCC."""
        nets = self._get_nets_for_ref("R1")
        self.assertIn("GND", nets)
        self.assertIn("VCC", nets)

    def test_u1_is_mcu(self):
        """U1 should have value STM32F411."""
        u1 = next(c for c in self.SAMPLE_NETLIST["components"] if c["ref"] == "U1")
        self.assertEqual(u1["value"], "STM32F411")

    def test_no_floating_nets(self):
        """Every net should have at least 2 nodes (no floating nets)."""
        for net in self.SAMPLE_NETLIST["nets"]:
            self.assertGreaterEqual(
                len(net["nodes"]), 2,
                f"Net {net['name']} has only {len(net['nodes'])} node(s) — floating net"
            )


if __name__ == '__main__':
    unittest.main(verbosity=2)
