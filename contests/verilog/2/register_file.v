module register_file #(
  parameter WIDTH = 4,
  parameter ADDRESS_WIDTH = 2
)(
  input wire clock,
  input wire we,
  input wire [ADDRESS_WIDTH-1:0] a0, a1, a2,
  input wire [WIDTH-1:0] wd,
  output wire [WIDTH-1:0] rd0, rd1
);

  reg [WIDTH-1:0] rf[0: (1<<ADDRESS_WIDTH)-1];

  always @(posedge clock) begin
    if (we) begin
      rf[a2] <= wd;
    end
  end

  assign rd0 = (a0 != 0) ? rf[a0] : 0;
  assign rd1 = (a1 != 0) ? rf[a1] : 0;

endmodule
