module and8
(
    input [7:0] yi_8,
    input ai_8,
    output [7:0] out_8
);
    and (out_8[0], yi_8[0], ai_8);
    and (out_8[1], yi_8[1], ai_8);
    and (out_8[2], yi_8[2], ai_8);
    and (out_8[3], yi_8[3], ai_8);
    and (out_8[4], yi_8[4], ai_8);
    and (out_8[5], yi_8[5], ai_8);
    and (out_8[6], yi_8[6], ai_8);
    and (out_8[7], yi_8[7], ai_8);
endmodule

module and64
(
    input [63:0] yi,
    input ai,
    output [63:0] out
);
    
    and8 and_1(  .out_8(out[7:0]),   .yi_8(yi[7:0]), .ai_8(ai));
    and8 and_2( .out_8(out[15:8]),  .yi_8(yi[15:8]), .ai_8(ai));
    and8 and_3(.out_8(out[23:16]), .yi_8(yi[23:16]), .ai_8(ai));
    and8 and_4(.out_8(out[31:24]), .yi_8(yi[31:24]), .ai_8(ai));
    and8 and_5(.out_8(out[39:32]), .yi_8(yi[39:32]), .ai_8(ai));
    and8 and_6(.out_8(out[47:40]), .yi_8(yi[47:40]), .ai_8(ai));
    and8 and_7(.out_8(out[55:48]), .yi_8(yi[55:48]), .ai_8(ai));
    and8 and_8(.out_8(out[63:56]), .yi_8(yi[63:56]), .ai_8(ai));
    
endmodule

module or8
(
    input [7:0] y8_0, y8_1, y8_2, y8_3,
    output [7:0] or_z8
);
    or (or_z8[0], y8_0[0], y8_1[0], y8_2[0], y8_3[0]);
    or (or_z8[1], y8_0[1], y8_1[1], y8_2[1], y8_3[1]);
    or (or_z8[2], y8_0[2], y8_1[2], y8_2[2], y8_3[2]);
    or (or_z8[3], y8_0[3], y8_1[3], y8_2[3], y8_3[3]);
    or (or_z8[4], y8_0[4], y8_1[4], y8_2[4], y8_3[4]);
    or (or_z8[5], y8_0[5], y8_1[5], y8_2[5], y8_3[5]);
    or (or_z8[6], y8_0[6], y8_1[6], y8_2[6], y8_3[6]);
    or (or_z8[7], y8_0[7], y8_1[7], y8_2[7], y8_3[7]);
endmodule

module or64
(
    input [63:0] y_0, y_1, y_2, y_3,
    output [63:0] or_z
);

    or8 or_1(.or_z8(  or_z[7:0]),   .y8_0(y_0[7:0]),   .y8_1(y_1[7:0]),   .y8_2(y_2[7:0]),   .y8_3(y_3[7:0]));
    or8 or_2(.or_z8( or_z[15:8]),  .y8_0(y_0[15:8]),  .y8_1(y_1[15:8]),  .y8_2(y_2[15:8]),  .y8_3(y_3[15:8]));
    or8 or_3(.or_z8(or_z[23:16]), .y8_0(y_0[23:16]), .y8_1(y_1[23:16]), .y8_2(y_2[23:16]), .y8_3(y_3[23:16]));
    or8 or_4(.or_z8(or_z[31:24]), .y8_0(y_0[31:24]), .y8_1(y_1[31:24]), .y8_2(y_2[31:24]), .y8_3(y_3[31:24]));
    or8 or_5(.or_z8(or_z[39:32]), .y8_0(y_0[39:32]), .y8_1(y_1[39:32]), .y8_2(y_2[39:32]), .y8_3(y_3[39:32]));
    or8 or_6(.or_z8(or_z[47:40]), .y8_0(y_0[47:40]), .y8_1(y_1[47:40]), .y8_2(y_2[47:40]), .y8_3(y_3[47:40]));
    or8 or_7(.or_z8(or_z[55:48]), .y8_0(y_0[55:48]), .y8_1(y_1[55:48]), .y8_2(y_2[55:48]), .y8_3(y_3[55:48]));
    or8 or_8(.or_z8(or_z[63:56]), .y8_0(y_0[63:56]), .y8_1(y_1[63:56]), .y8_2(y_2[63:56]), .y8_3(y_3[63:56])); 
   
endmodule

module mux64_4_2
(
    input wire [63:0] y0, y1, y2, y3,
    input wire [1:0] x,
    output wire [63:0] z
);

    wire not_x0, not_x1;
    wire a0, a1, a2, a3;
    wire [63:0] b0, b1, b2, b3;
    
    not (not_x0, x[0]);
    not (not_x1, x[1]);
    and (a0, not_x1, not_x0);
    and (a1, not_x1, x[0]);
    and (a2, x[1], not_x0);
    and (a3, x[1], x[0]);
    
    and64 and_ab1(.out(b0), .yi(y0), .ai(a0));
    and64 and_ab2(.out(b1), .yi(y1), .ai(a1));
    and64 and_ab3(.out(b2), .yi(y2), .ai(a2));
    and64 and_ab4(.out(b3), .yi(y3), .ai(a3));
    
    or64 or1(.or_z(z), .y_0(b0), .y_1(b1), .y_2(b2), .y_3(b3));

endmodule
