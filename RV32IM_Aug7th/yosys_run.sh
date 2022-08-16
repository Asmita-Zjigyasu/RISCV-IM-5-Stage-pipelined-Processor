# read design

read_verilog iiitb_riscv.v #your design

# generic synthesis
synth -top top #name of the top module

# mapping to mycells.lib
dfflibmap -liberty /home/ubuntu/Desktop/Gate_Level_Synthesis/RV32IM/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

abc -liberty /home/ubuntu/Desktop/Gate_Level_Synthesis/RV32IM/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
clean
flatten
# write synthesized design
write_verilog -noattr synth_riscv.v #name you wish to give for the genrated netlist.
#Here the flag -noattr removes the annotations in the generated file.