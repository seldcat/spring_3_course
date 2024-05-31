module jk_trigger(
    input j, 
    input k, 
    input clock,
    output reg q, 
    output reg q_bar
);

    wire and_g1, and_g2, nand_g3, nand_g4;

    and and_g1_inst(and_g1, j, clock);
    and and_g2_inst(and_g2, k, clock);
    nand nand_g3_inst(nand_g3, and_g1, and_g1);
    nand nand_g4_inst(nand_g4, and_g2, and_g2);
    nand nand_g5_inst(q, nand_g3, q_bar);
    nand nand_g6_inst(q_bar, nand_g4, q);
endmodule

module d_trigger(
    input d, 
    input clock,
    output reg q, 
    output reg q_bar
);

    wire not_g1;
  
    not not_g1_inst(not_g1, d);
    jk_trigger jk(
        .j(d),
        .k(not_g1),
        .clock(clock),
        .q(q),
        .q_bar(q_bar)
    );
endmodule
