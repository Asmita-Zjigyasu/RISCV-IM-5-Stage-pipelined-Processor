# RISCV-IM-5-Stage-pipelined-Processor
This repository describes the information needed to build a five-stage RISC-V pipelined core, which has the upport of base interger RV32I instruction format and Multiplication instruction format using Nmigen. 

# Introduction 
RISC-V has been designed to support extensive customization and specialization. The base integer ISA can be extended with one or more optional instruction-set extensions, but the base integer instructions cannot be redefined. We have implemented the Multiplication extension of the same, taking into consideration stalling, forwarding and branching for optimized utilisation of the space and clock cycles.\

**RISC-V base instruction format is shown below** : 
![Image](https://github.com/Asmita-Zjigyasu/RISCV-IM-5-Stage-pipelined-Processor/blob/main/Images/riscv%20instruction%20description.gif "RISC-V base instruction formats")

![Image](https://github.com/Asmita-Zjigyasu/RISCV-IM-5-Stage-pipelined-Processor/blob/main/Images/riscv%20instructions%20set.gif "RISC-V base instruction set") 

# Design Description
1. This is a 5 stage pipelined processor based on RISCV architecture, which supports Integer arithematic operations and has been extended to accomodate Multiplication set of instructions as well.
2. The processor has been coded in Nmigen library of Python. This has been done because Python is very easy to understand. The Nmigen code can be converted to Verilog by 2 commands, which are stated ahead.
3. The 5 stages in the processor are - fetch, decode, execute, memory, writeback. All the stages are integrated using a Wrapper module.
4. This is a 32 bit processor with 1024 memory locations of both instruction memory and data memory.
5. It includes implementation of stall, forwarding and branching conditions while taking care of majority of the corner cases by performing extensive program testing. Several C programs have been converted to RISCV assembly using the RISCV GNU Toolchain and have been tested on the processor code with successful results. The C programs range from a simple ADD program (c=a+b) to a merge sort program for sorting 7 numbers.
6. Few of the many RV32I base instruction set descriptions can be found in the screenshot below:
//image of the riscv instruction set//

# Application
We plan to use the processor to build a full-fleged System on Chip design. This can be used to build a RISCduino if the correct and compatible peripherals are integrated with the processor. The RISCV procossor will be the core of the micro-controller.

# Block Diagram
![Image](https://github.com/Asmita-Zjigyasu/RISCV-IM-5-Stage-pipelined-Processor/blob/main/Images/block%20diagram.gif)

# Tool installation Details
## iVerilog : 
Icarus Verilog is an implementation of the Verilog hardware description language.

## GTKWave : 
GTKWave is a VCD waveform viewer based on the GTK library. This viewer support VCD and LXT formats for signal dumps. Waveform dumps are written by the Icarus Verilog runtime program vvp. The user uses $dumpfile and $dumpvars system tasks to enable waveform dumping, then the vvp runtime takes care of the rest. 

To download iVerilog and GTKWave in Ubuntu, use the following commands:
```
sudo apt-get update
sudo apt-get install iverilog gtkwave
```

## Nmigen : 
Despite being faster than schematics entry, hardware design with Verilog and VHDL remains tedious and inefficient for several reasons. Nmigen enables hardware designers to take advantage of the richness of the Python language—object oriented programming, function parameters, generators, operator overloading, libraries, etc.—to build well organized, reusable and elegant designs.\
To install Nmigen, follow the steps in the [Robert Baruch Nmigen Installation repository](https://github.com/RobertBaruch/nmigen-tutorial/blob/master/1_install.md).

## GNU Toolchain : 
The GNU Toolchain is a set of programming tools in Linux systems that programmers can use to make and compile their code to produce a program or library. So, here we use the RISCV GNU Toolchain to generate the RISCV Assembly for any C code.\
RISCV GNU Toolchain can be installed from [this repository](https://github.com/shivanishah269/risc-v-core#overview-of-gnu-compiler-toolchain).

# Functional Simulation
Run the following commands on terminal to run the verilog file with testbench to get a .vcd file output:

```
1. python3 Wrapper_class.py>wrapper.v  
2. iverilog wrapper.v test.v 
3. ./a.out 
4. gtkwave test.vcd
```

## Screenshot
![Image](https://github.com/Asmita-Zjigyasu/iiitb_riscv32im5/blob/main/Images/Pre-synthesis_simulation.png)

# Functional characteristics
![Image](https://github.com/Asmita-Zjigyasu/RISCV-IM-5-Stage-pipelined-Processor/blob/main/Images/stages.gif)
## STAGES:
1. **Instruction Fetch**: IF module takes Program Counter as Input from Wrapper module and gives out the 32-bit Instruction which will be forwarded to the Decode stage for processing.
2. **Decode (ID)**: RV32IM has 7 types of instructions namely R, I, S, B, U, J, and M types differentiated by opcodes. According to each type, the source register, destination register and/or immediate field are extracted from the instruction. The extracted data is passed to Execute Stage.
3. **Execute**: Execute stage performs arithmetic and logical operations based on the opcode. Ra, Rb and/or sign-extended immediate field will be the parameters of the EX stage.
4. **Memory File**: Memory is accessed in this stage if required. This stage is accessed only by the load and the store instruction to extract or stare data into the memory. For load instruction, it loads an operand from the memory and for the store instruction, it would store an operand into the memory. 
5. **Register File**: The register file stores the data of all the registers of the processor. It is accessed in the ID stage and in the Write-back stage to extract data from the registers and to write to them. Data is written in the positive half of the cycle so that we read the updated data in the negative half of the clock cycle. We write data in the positive half of the cycle so that we read the updated data in the negative half of the clock cycle. 
## WRAPPER MODULE:
The wrapper module connects the 5 stages and makes the
processor work. It can be majorly divided into 4 units.
1. **Control Unit**: The control unit interlinks all 5 stages by connecting the outputs of one stage to the inputs of the other stage. It manages the communication of control signals to all other stages. The control signals determine how to process input data.
2. **Forwarding Unit**: Forwarding unit helps to reduce the overall CPI (clock cycles per instruction) of the processor. To accommodate this dependencies, the forwarding unit passes the data from the stage where it is available to the stage where it is required.
3. **Stalling Unit**: The functionality of this unit is to wait when there are dependencies between the instructions. It introduces NOP instruction between the instructions which have dependencies.
4. **Flushing Unit**: As this is a pipelined processor, by the time when the branching condition is checked in the EX stage, 2 instructions are already fetched. If the branch is taken, which is decided at the start of the MEM stage, the 3 fetched instructions need to be flushed out by the Flushing unit so that unnecessary changes are not made to the memory or register file.

The processor has been tested on several C programs, providing the correct output. The complete testing process has been expalined in [this document](https://docs.google.com/document/d/1JXD6lvziDR5GNDnnr6U30ztoxr11s2_hYlZX54NLtvs/edit?usp=sharing).

# Synthesis:
## Yosys installation for Ubuntu
1. Clone the [this](https://github.com/YosysHQ/yosys) GitHub repository.
2. Execute the following set of commands
```
1. make
2. sudo apt install make
3. sudo apt-get install build-essential clang bison flex \
    libreadline-dev gawk tcl-dev libffi-dev git \
    graphviz xdot pkg-config python3 libboost-system-dev \
    libboost-python-dev libboost-filesystem-dev zlib1g-dev
4 . make
5. sudo make install.

```
## Steps for generating the netlist
1. Clone [this](https://github.com/kunalg123/sky130RTLDesignAndSynthesisWorkshop) GitHub repository
2. Change the yosys_run.sh script with your design. 
3. Check the reference script in this repo.
4. Type yosys in the terminal which opens an interactive command shell.
5. Execute the following command which synthesizes your design and generates a gate-level netlist.
```
script yosys_run.sh
```
6. We can view the statistics of the netlist by typing "stat".
## Screenshots of the statistics of our design iiitb_riscv32im5
![Image](https://github.com/Asmita-Zjigyasu/iiitb_riscv32im5/blob/main/Images/stat_1.png)
![Image](https://github.com/Asmita-Zjigyasu/iiitb_riscv32im5/blob/main/Images/stat_2.png)

7. To test the post synthesis design execute the following commands
```
iverilog -DFUNCTIONAL -DUNIT_DELAY=#1 synth_riscv.v iiitb_riscv_tb.v primitives.v sky130_fd_sc_hd.v
./a.out
gtkwave test.vcd
```
## Post synthesis simulation
![Image](https://github.com/Asmita-Zjigyasu/iiitb_riscv32im5/blob/main/Images/Post_synthesis_simulation.png)
* We can observe that the simulation results are same as before synthesis.



# Contibutors
* Mayank Kabra, Student, IIIT Bangalore
* Asmita Zjigyasu, Student, IIIT Bangalore
* Saketh Gajawada, Student, IIIT Bangalore
* Yathin Kumar, Student, IIIT Bangalore
* Oishi Seth, Student, IIIT Bangalore

# Acknowledgements
* Kunal Ghosh, Director, VSD Corp. Pvt. Ltd.

# Contact Information
* [Mayank Kabra](mailto:Mayank.Kabra@iiitb.ac.in?subject=[GitHub]%20ASIC%20Course)
* [Asmita Zjigyasu](mailto:Asmita.Zjigyasu@iiitb.ac.in?subject=[GitHub]%20ASIC%20Course)
* [Saketh Gajawada](mailto:Saketh.Gajawada@iiitb.ac.in?subject=[GitHub]%20ASIC%20Course)
* [Yathin Kumar](mailto:Yathin.Kumar@iiitb.ac.in?subject=[GitHub]%20ASIC%20Course)
* [Oishi Seth](mailto:Oishi.Seth@iiitb.ac.in?subject=[GitHub]%20ASIC%20Course)
* [Kunal Ghosh](kunalghosh@gmail.com)

# References
* [GNU Toolchain and RISCV overview](https://github.com/shivanishah269/risc-v-core)
* [RISCV Manual](https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf)
* [Robert Baruch Nmigen Tutorial](https://github.com/RobertBaruch/nmigen-tutorial)
* [Function calls](https://github.com/riscv-collab/riscv-gnu-toolchain/issues/1088)








