`timescale 1ns/1ps
module Wrapper_tb;

reg clk;
reg rst;
wire [31:0] data_out;

top top_tb(
    .clk(clk),
    .rst(rst),
    .data_out(data_out)
);

initial begin
clk=0;
forever #10 clk=~clk;
end

initial begin
$dumpfile("test.vcd");
$dumpvars(0,Wrapper_tb);

rst=1;
#100;
rst=0;

#2000 $finish;

end
endmodule
