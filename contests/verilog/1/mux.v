module mux
#( 
    parameter DATA_WIDTH = 8,
    parameter ADDRESS_WIDTH = 2
)
(
    input [((2**ADDRESS_WIDTH)*DATA_WIDTH)-1:0] data_in,
    input [ADDRESS_WIDTH-1:0] address,
    output [DATA_WIDTH-1:0] data_out
);

    wire [DATA_WIDTH-1:0] tmp_array [0:(2**ADDRESS_WIDTH)-1];
    genvar i;
    generate
        for(i=0; i<2**ADDRESS_WIDTH; i=i+1) begin: gen_array
            assign tmp_array[i] = data_in[((i+1)*DATA_WIDTH)-1:(i*DATA_WIDTH)];
        end
    endgenerate
    assign data_out = tmp_array[address];
endmodule
