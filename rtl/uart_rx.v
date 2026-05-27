// uart_rx.v
// UART Receiver — 8N1 format, configurable baud rate
// Uses 16x oversampling for robust bit detection
//
// SPDX-License-Identifier: MIT
// Copyright (c) 2026 EmbeddedOS Foundation

`timescale 1ns / 1ps

module uart_rx #(
    parameter CLK_FREQ  = 50_000_000,
    parameter BAUD_RATE = 115_200
) (
    input  wire       clk,
    input  wire       rst_n,
    input  wire       rx,
    output reg  [7:0] rx_data,
    output reg        rx_valid,   // Pulses high for 1 cycle when byte received
    output reg        rx_error    // Framing error (stop bit not high)
);

    // 16x oversampling: sample at 16× baud rate, latch at sample 8
    localparam OVERSAMPLE    = 16;
    localparam BAUD_DIV      = CLK_FREQ / (BAUD_RATE * OVERSAMPLE);
    localparam SAMPLE_POINT  = OVERSAMPLE / 2;   // Sample at mid-bit

    localparam IDLE  = 2'd0;
    localparam START = 2'd1;
    localparam DATA  = 2'd2;
    localparam STOP  = 2'd3;

    reg [1:0]  state;
    reg [15:0] clk_cnt;      // Clock divider counter
    reg [3:0]  sample_cnt;   // Oversample counter (0–15)
    reg [2:0]  bit_idx;      // Data bit index
    reg [7:0]  shift_reg;
    reg        rx_sync;      // Synchronized RX input

    // Synchronize RX input to avoid metastability
    reg rx_meta;
    always @(posedge clk) begin
        rx_meta <= rx;
        rx_sync <= rx_meta;
    end

    always @(posedge clk) begin
        if (!rst_n) begin
            state      <= IDLE;
            clk_cnt    <= 0;
            sample_cnt <= 0;
            bit_idx    <= 0;
            shift_reg  <= 0;
            rx_data    <= 0;
            rx_valid   <= 0;
            rx_error   <= 0;
        end else begin
            rx_valid <= 0;
            rx_error <= 0;

            if (clk_cnt == BAUD_DIV - 1) begin
                clk_cnt <= 0;

                case (state)

                    IDLE: begin
                        if (!rx_sync) begin
                            // Falling edge detected — possible start bit
                            sample_cnt <= 1;
                            state      <= START;
                        end
                    end

                    START: begin
                        sample_cnt <= sample_cnt + 1;
                        if (sample_cnt == SAMPLE_POINT) begin
                            if (!rx_sync) begin
                                // Confirmed start bit at mid-point
                                bit_idx    <= 0;
                                sample_cnt <= 0;
                                state      <= DATA;
                            end else begin
                                // False start — return to idle
                                state <= IDLE;
                            end
                        end
                    end

                    DATA: begin
                        sample_cnt <= sample_cnt + 1;
                        if (sample_cnt == OVERSAMPLE - 1) begin
                            sample_cnt         <= 0;
                            shift_reg[bit_idx] <= rx_sync;
                            if (bit_idx == 7) begin
                                state <= STOP;
                            end else begin
                                bit_idx <= bit_idx + 1;
                            end
                        end
                    end

                    STOP: begin
                        sample_cnt <= sample_cnt + 1;
                        if (sample_cnt == OVERSAMPLE - 1) begin
                            sample_cnt <= 0;
                            state      <= IDLE;
                            if (rx_sync) begin
                                // Valid stop bit
                                rx_data  <= shift_reg;
                                rx_valid <= 1;
                            end else begin
                                // Framing error
                                rx_error <= 1;
                            end
                        end
                    end

                    default: state <= IDLE;

                endcase
            end else begin
                clk_cnt <= clk_cnt + 1;
            end
        end
    end

endmodule
