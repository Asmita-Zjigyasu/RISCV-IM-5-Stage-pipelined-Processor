from typing import List

from nmigen import *
from nmigen.sim import *
#from nmigen.sim import *
from nmigen import Elaboratable, Module, Signal
from nmigen.build import Platform
from nmigen_soc.memory import *
from nmigen_soc.wishbone import *



class IF_stage(Elaboratable):

    def __init__(self):
        self.data = Memory( width = 32, depth = 23, init = [

0,0xfd010113,
0x02812623,
0x03010413,
0x00500793,
0xfef42623,
0x00500793,
0xfef42423,
0xfec42703,
0xfe842783,
0x00f707b3,
0xfef42223,
0xfe842703,
0xfe442783,
0x00f707b3,
0xfef42023,
0xfe442703,
0xfe042783,
0x00f707b3,
0xfcf42e23,
0x00000013,
0x02c12403,
0x03010113])
        self.Pc = Signal(10)
        self.out = Signal(32)
      

    def elaborate(self, platform: Platform) -> Module:
        m = Module()
        # Register the read port submodule.
        m.d.sync += self.out.eq(self.data[self.Pc])
        return m

    def ports(self):
        return []


# def rom_read_ut( rom, address, expected ):
#   # Set address, and wait a tick.
#   yield rom.adr.eq( address )
#   yield Tick()
#   # Done. Check the result after combinatorial logic settles.
#   yield Tick()
#   actual = yield rom.dat_r
#   if expected == actual:
#     print( "PASS: Memory[ 0x%04X ] = 0x%08X"%( address, expected ) )
#   else:
#     print( "FAIL: Memory[ 0x%04X ] = 0x%08X (got: 0x%08X)"
#            %( address, expected, actual ) )

# if __name__ == "__main__":
#   # Create a test memory with 20 bytes of data.
#   dut = IF_stage( [ 0x01234567, 0x89ABCDEF,
#                0x0C0FFEE0, 0xDEC0FFEE,
#                0xFEEBEEDE ] )
  # Run the simulation.
  # with Simulator( dut, vcd_file = open( 'rom.vcd', 'w' ) ) as sim:
  #   def proc():
  #     # Test reads.
  #     yield from rom_read_ut( dut, 0, 0x01234567 )
  #     yield from rom_read_ut( dut, 1, 0x89ABCDEF )
  #     yield from rom_read_ut( dut, 2, 0x0C0FFEE0 )
  #     yield from rom_read_ut( dut, 3, 0xDEC0FFEE )
  #     yield from rom_read_ut( dut, 4, 0xFEEBEEDE )
  #   sim.add_clock( 1e-6 )
  #   sim.add_sync_process( proc )
  #   sim.run()

# if __name__ == "__main__":
#     n = Module()
#     n.domains.sync = sync = ClockDomain("sync", async_reset=True)

#     n.submodules.if_stage = if_stage = IF_stage()
#     Pc = Signal(5)
   
#     n.d.sync += if_stage.Pc.eq(Pc)

#     with Simulator( if_stage) as sim:
#       def proc():
#         yield Pc.eq(0b00000)
#         yield

#         yield Pc.eq(0b00001)
#         yield

#         yield Pc.eq(0b00010)
#         yield
#       sim.add_clock( 1e-6 )
#       sim.add_sync_process( proc )
#       sim.run()

    # sim = Simulator(n)
    # sim.add_clock(1e-6, domain="sync")

    # def process():
        

# sim.add_sync_process(process,domain = "sync")
# sim.add_sync_process(process)
# with sim.write_vcd("alu.vcd","alu.gtkw",traces=[reg_addr_in,Ra,Rb,inst_type,inst_type1,inst_type2,immediate,inst_type3]+alu.ports()):
#    sim.run_until(100e-6, run_passive=True)


       

