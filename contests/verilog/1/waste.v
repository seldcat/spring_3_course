module prefix_adder #(parameter LEVELS = 2) (
    input [(2**LEVELS)-1:0] x,
    input [(2**LEVELS)-1:0] y,
    input carry_in,
    output [(2**LEVELS)-1:0] z,
    output carry_out
);
    localparam WIDTH = 2**LEVELS;
    wire [WIDTH-1:0] g, p, c;

    genvar i;
    generate
        for (i = 0; i < WIDTH; i = i + 1) begin : gp
            assign g[i] = x[i] & y[i];
            assign p[i] = x[i] ^ y[i];
        end
    endgenerate

    assign c[0] = carry_in;
    generate
        for (i = 1; i < WIDTH; i = i + 1) begin : carry_lookahead
            assign c[i] = g[i-1] | (p[i-1] & c[i-1]);
        end
    endgenerate

    generate
        for (i = 0; i < WIDTH; i = i + 1) begin : sum
            assign z[i] = p[i] ^ c[i];
        end
    endgenerate

    assign carry_out = g[WIDTH-1] | (p[WIDTH-1] & c[WIDTH-1]);

endmodule