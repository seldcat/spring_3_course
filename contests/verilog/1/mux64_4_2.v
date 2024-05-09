module mux64_4_2(
    input      [63:0] y0,
    input      [63:0] y1,
    input      [63:0] y2,
    input      [63:0] y3,
    input       [1:0]  x,
    output reg [63:0]  z
);

// Создаем временные сигналы для хранения результатов выбора
wire [63:0] temp0, temp1, temp2, temp3;

// Присваиваем значения временным сигналам в зависимости от x
assign temp0 =  (x[1] & ~x[0]) ? y0 : 64'b0;
assign temp1 =  (~x[1] & x[0]) ? y1 : 64'b0;
assign temp2 =   (x[1] & x[0]) ? y2 : 64'b0;
assign temp3 = (~x[1] & ~x[0]) ? y3 : 64'b0;

// Присваиваем z результат выбора в зависимости от x
assign z = temp0 | temp1 | temp2 | temp3;

endmodule

