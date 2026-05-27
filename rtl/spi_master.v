// spi_master.v
// SPI Master — Mode 0 (CPOL=0, CPHA=0), configurable clock divider
//
// Parameters:
//   CLK_DIV : Clock divider (SPI_CLK = SYS_CLK / (2 * CLK_DIV))
//
// SPDX-License-Identifier: MIT
// Copyright (c) 2026 EmbeddedOS Foundation

`timescale 1ns / 1ps

module spi_master #(
    parameter CLK_DIV = 4,
    parameter DATA_WIDTH = 8
) (
    input  wire                   clk,
    input  wire                   rst_n,
    // Control interface
    input  wire [DATA_WIDTH-1:0]  tx_data,
    input  wire                   tx_valid,
    output reg  [DATA_WIDTH-1:0]  rx_data,
    output reg                    rx_valid,
    output reg                    busy,
    // SPI interface
    output reg                    sclk,
    output reg                    mosi,
    input  wire                   miso,
    output reg                    cs_n
);

    localparam IDLE     = 2'd0;
    localparam TRANSFER = 2'd1;
    localparam DONE     = 2'd2;

    reg [1:0]                  state;
    reg [$clog2(CLK_DIV)-1:0]  clk_cnt;
    reg [$clog2(DATA_WIDTH):0] bit_cnt;
    reg [DATA_WIDTH-1:0]       shift_tx;
    reg [DATA_WIDTH-1:0]       shift_rx;
    reg                        clk_phase;

    always @(posedge clk) begin
        if (!rst_n) begin
            state     <= IDLE;
            clk_cnt   <= 0;
            bit_cnt   <= 0;
            shift_tx  <= 0;
            shift_rx  <= 0;
            clk_phase <= 0;
            sclk      <= 0;
            mosi      <= 0;
            cs_n      <= 1;
            busy      <= 0;
            rx_valid  <= 0;
            rx_data   <= 0;
        end else begin
            rx_valid <= 0;

            case (state)

                IDLE: begin
                    sclk  <= 0;
                    cs_n  <= 1;
                    busy  <= 0;
                    if (tx_valid) begin
                        shift_tx  <= tx_data;
                        bit_cnt   <= DATA_WIDTH - 1;
                        clk_cnt   <= 0;
                        clk_phase <= 0;
                        cs_n      <= 0;
                        busy      <= 1;
                        state     <= TRANSFER;
                    end
                end

                TRANSFER: begin
                    if (clk_cnt == CLK_DIV - 1) begin
                        clk_cnt   <= 0;
                        clk_phase <= ~clk_phase;

                        if (!clk_phase) begin
                            // Rising edge: sample MISO
                            sclk              <= 1;
                            shift_rx          <= {shift_rx[DATA_WIDTH-2:0], miso};
                        end else begin
                            // Falling edge: shift out MOSI
                            sclk <= 0;
                            mosi <= shift_tx[bit_cnt];
                            if (bit_cnt == 0) begin
                                state <= DONE;
                            end else begin
                                bit_cnt <= bit_cnt - 1;
                            end
                        end
                    end else begin
                        clk_cnt <= clk_cnt + 1;
                    end
                end

                DONE: begin
                    cs_n     <= 1;
                    sclk     <= 0;
                    rx_data  <= shift_rx;
                    rx_valid <= 1;
                    busy     <= 0;
                    state    <= IDLE;
                end

                default: state <= IDLE;

            endcase
        end
    end

endmodule
