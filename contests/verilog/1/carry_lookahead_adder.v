module carry_lookahead_generator
# (
    parameter WIDTH = 8
)
(
    input                  carry_input,
    input    [ WIDTH-1:0 ] generate_in, propagate_in,
    output   [ WIDTH  :0 ] carry,
    output                 group_generate, group_propagate
);
    
    wire     [ WIDTH-1:0 ] g_temp;
    
    assign carry[ 0 ] = carry_input;
    
    generate
        
        genvar i;
        
        for (i = 0; i <= WIDTH-1; i = i+1)
        begin : stage
            assign carry[ i+1 ] = generate_in[ i ] | propagate_in[ i ] & carry[ i ];
            case( i )
                WIDTH-1 : assign g_temp[ i ] = generate_in[ i ];
                default   : assign g_temp[ i ] = ( & propagate_in[ WIDTH-1:i+1 ] ) & generate_in[ i ];
            endcase
        end
    endgenerate
    
    assign group_propagate = & propagate_in;
    assign group_generate  = | g_temp;

endmodule



module carry_lookahead_adder
# (
    parameter WIDTH = 8
)
(
    input                  carry_in,
    input    [ WIDTH-1:0 ] x,
    input    [ WIDTH-1:0 ] y,
    output   [ WIDTH-1:0 ] z,
    output                 carry_out
);
    wire [ WIDTH:0 ] carry;
    
    wire [ WIDTH-1:0 ] generate_wire, propagate_wire; 
    
        carry_lookahead_generator
    # ( .WIDTH( WIDTH ) )
    i_carry_lookahead_generator
    (
        .carry_input    ( carry_in       ),
        .generate_in    ( generate_wire  ),
        .propagate_in   ( propagate_wire ),
        .carry          ( carry          ),
        .group_propagate(),
        .group_generate ()
    );
    
    generate
        
        genvar i;
        
        for (i = 0; i <= WIDTH-1; i = i+1)
        begin : stage
            assign generate_wire [ i ] = x[ i ] & y[ i ];
            assign propagate_wire[ i ] = x[ i ] ^ y[ i ];

            assign z[ i ] = carry[ i ] ^ propagate_wire[ i ];
        end
    endgenerate
    
    assign carry_out = carry[ WIDTH ];

endmodule
