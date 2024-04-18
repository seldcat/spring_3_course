module mux64_4_2(
    input [63:0] y0,
    input [63:0] y1,
    input [63:0] y2,
    input [63:0] y3,
    input [1:0] x,
    output reg [63:0] z
);

always @(*) begin
    case(x)
        2'b00: z = y0;
        2'b01: z = y1;
        2'b10: z = y2;
        2'b11: z = y3;
        default: z = 64'b0;
    endcase
end

endmodule

