#!/usr/bin/env python

from imem import Instr_Mem
from dmem import Data_Mem
from sim import Simulator

imem = Instr_Mem("imem.txt")
dmem = Data_Mem("dmem.txt")
sim = Simulator(imem.output_array(), dmem.output_array())

print "Simulation for Small16 Processor has begun.\n" + \
  "Data memory is set in dmem.txt\n" + \
  "Instruction memory is set in imem.txt\n" + \
  "\nInstructions to use Simulator object:\n" + \
  "sim.step(N)            Steps program N instructions, default is 1.\n" + \
  "sim.run()              Steps program until finished.\n" + \
  "sim.restart(N)         Restarts the program and steps N instructions.\n" + \
  "sim.output_reg()       Outputs register values.\n" + \
  "sim.output_dmem(M, N)  Outputs data memory starting at index M with range N.\n" + \
  "sim.output_imem(M, N)  Outputs instruction memory starting at index M with range N.\n" + \
  "sim.output_instr_cnt()  Outputs the number of times each instruction has been executed."
