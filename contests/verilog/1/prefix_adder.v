module prefix_adder
#(
    parameter LEVELS = 3,
    parameter WIDTH  = 2 ** LEVELS
)
(
    input                    carry_in,
    input  [ WIDTH - 1 : 0 ]     x, y,
    output [ WIDTH - 1 : 0 ]        z,
    output                   carry_out
);
    wire [ WIDTH : 0 ] g_temp, p_temp, c_temp;

    genvar i, j;
    generate
        for (i = 0; i < WIDTH; i = i + 1) begin: stages_1
            assign g_temp[i] = x[i] & y[i];
            assign p_temp[i] = x[i] ^ y[i];
        end
    endgenerate

    generate
        for (i = 0; i < WIDTH; i = i + 1) begin: stages_2
            if (i == 0)
                assign c_temp[i] = carry_in;
            else
                assign c_temp[i] = g_temp[i-1] | (p_temp[i-1] & c_temp[i-1]);
            assign z[i] = p_temp[i] ^ c_temp[i];
        end
    endgenerate

    assign carry_out = g_temp[ WIDTH - 1 ] | (p_temp[ WIDTH - 1 ] & c_temp[ WIDTH - 1 ]);
endmodule
