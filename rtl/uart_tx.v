// uart_tx.v
// UART Transmitter — 8N1 format, configurable baud rate
//
// Parameters:
//   CLK_FREQ  : System clock frequency in Hz (default 50 MHz)
//   BAUD_RATE : UART baud rate (default 115200)
//
// Ports:
//   clk       : System clock (rising edge)
//   rst_n     : Active-low synchronous reset
//   tx_data   : 8-bit data to transmit
//   tx_valid  : Pulse high for 1 cycle to start transmission
//   tx_ready  : High when transmitter is idle and ready
//   tx        : UART TX output line
//
// SPDX-License-Identifier: MIT
// Copyright (c) 2026 EmbeddedOS Foundation

`timescale 1ns / 1ps

module uart_tx #(
    parameter CLK_FREQ  = 50_000_000,
    parameter BAUD_RATE = 115_200
) (
    input  wire       clk,
    input  wire       rst_n,
    input  wire [7:0] tx_data,
    input  wire       tx_valid,
    output reg        tx_ready,
    output reg        tx
);

    // Baud rate divider: number of clock cycles per bit
    localparam BAUD_DIV = CLK_FREQ / BAUD_RATE;

    // State machine
    localparam IDLE  = 2'd0;
    localparam START = 2'd1;
    localparam DATA  = 2'd2;
    localparam STOP  = 2'd3;

    reg [1:0]  state;
    reg [15:0] baud_cnt;    // Baud rate counter
    reg [2:0]  bit_idx;     // Current data bit index (0–7)
    reg [7:0]  shift_reg;   // Data shift register

    always @(posedge clk) begin
        if (!rst_n) begin
            state    <= IDLE;
            baud_cnt <= 0;
            bit_idx  <= 0;
            shift_reg<= 8'h00;
            tx       <= 1'b1;   // Idle line is high
            tx_ready <= 1'b1;
        end else begin
            case (state)

                IDLE: begin
                    tx       <= 1'b1;
                    tx_ready <= 1'b1;
                    if (tx_valid) begin
                        shift_reg <= tx_data;
                        baud_cnt  <= 0;
                        state     <= START;
                        tx_ready  <= 1'b0;
                    end
                end

                START: begin
                    tx <= 1'b0;   // Start bit (low)
                    if (baud_cnt == BAUD_DIV - 1) begin
                        baud_cnt <= 0;
                        bit_idx  <= 0;
                        state    <= DATA;
                    end else begin
                        baud_cnt <= baud_cnt + 1;
                    end
                end

                DATA: begin
                    tx <= shift_reg[bit_idx];   // LSB first
                    if (baud_cnt == BAUD_DIV - 1) begin
                        baud_cnt <= 0;
                        if (bit_idx == 7) begin
                            state <= STOP;
                        end else begin
                            bit_idx <= bit_idx + 1;
                        end
                    end else begin
                        baud_cnt <= baud_cnt + 1;
                    end
                end

                STOP: begin
                    tx <= 1'b1;   // Stop bit (high)
                    if (baud_cnt == BAUD_DIV - 1) begin
                        baud_cnt <= 0;
                        state    <= IDLE;
                        tx_ready <= 1'b1;
                    end else begin
                        baud_cnt <= baud_cnt + 1;
                    end
                end

                default: state <= IDLE;

            endcase
        end
    end

endmodule
