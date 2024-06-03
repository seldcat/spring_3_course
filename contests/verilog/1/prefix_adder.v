module prefix
#(
    parameter LEVELS = 1,
    parameter WIDTH = 2**LEVELS
)
(
    input [WIDTH-1:0] x, y,
    input [1:0] in_pg,
    output [WIDTH-1:0] pw, gw,
    output [1:0] out_pg
);
    generate
        genvar i;
        if (LEVELS == 1) begin
            wire [WIDTH:0] g, p;
            assign g[0] = in_pg[0];
            assign p[0] = in_pg[1];
            for (i = 1; i <= WIDTH; i = i + 1) begin
                assign p[i] = x[i-1] | y[i-1];
                assign g[i] = x[i-1] & y[i-1];
            end
            assign pw[0] = p[0];
            assign gw[0] = g[0];
            assign pw[1] = p[1] & p[0];
            assign gw[1] = g[1] | (p[1] & g[0]);
            assign out_pg[1] = p[2];
            assign out_pg[0] = g[2];
        end else begin
            wire [1:0] temp_pg;
            wire [WIDTH-1:0] temp_pw, temp_gw;
            prefix #(.LEVELS(LEVELS-1)) pr1 (
                .x(x[WIDTH/2-1:0]),
                .y(y[WIDTH/2-1:0]),
                .in_pg(in_pg),
                .pw(temp_pw[WIDTH/2-1:0]),
                .gw(temp_gw[WIDTH/2-1:0]),
                .out_pg(temp_pg)
            );
            prefix #(.LEVELS(LEVELS-1)) pr2 (
                .x(x[WIDTH-1:WIDTH/2]),
                .y(y[WIDTH-1:WIDTH/2]),
                .in_pg(temp_pg),
                .pw(temp_pw[WIDTH-1:WIDTH/2]),
                .gw(temp_gw[WIDTH-1:WIDTH/2]),
                .out_pg(out_pg)
            );
            for (i = 0; i < WIDTH/2; i = i + 1) begin
                assign pw[i] = temp_pw[i];
                assign gw[i] = temp_gw[i];
            end
            for (i = WIDTH/2; i < WIDTH; i = i + 1) begin
                assign pw[i] = temp_pw[i] & temp_pw[WIDTH/2-1];
                assign gw[i] = temp_gw[i] | (temp_pw[i] & temp_gw[WIDTH/2-1]);
            end
        end
    endgenerate
endmodule


module prefix_adder
#(
    parameter LEVELS = 2,
    parameter WIDTH = 2**LEVELS
)
(
    input [WIDTH-1:0] x, y,
    input carry_in,
    output [WIDTH-1:0] z,
    output carry_out
);
    wire [1:0] pg;
    wire [WIDTH-1:0] pw, gw;
    prefix #(.LEVELS(LEVELS)) pr (
        .x(x),
        .y(y),
        .in_pg({1'b1, carry_in}),
        .pw(pw),
        .gw(gw),
        .out_pg(pg)
    );
    generate
        genvar i;
        for (i = 0; i < WIDTH; i = i + 1) begin
            assign z[i] = gw[i] ^ (x[i] ^ y[i]);
        end
    endgenerate
    assign carry_out = (pg[1] & gw[WIDTH-1]) | pg[0];
endmodule
