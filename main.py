#!/usr/bin/env python

from imem import Instr_Mem
from dmem import Data_Mem
from sim import Simulator

imem = Instr_Mem("imem.txt")
dmem = Data_Mem("dmem.txt")
prog1 = Simulator(imem.output_array(), dmem.output_array())

while True:
  print "(1) Run the entire program\n"
  print "(2) Run a specified number of steps\n"
  print "(q) Quit"

  userSelection = raw_input()
  if userSelection == 1
    prog1.run(self)
  elif userSelection == 2
    steps = raw_input("Enter number of steps to run: ")
    prog1.step(self, steps)
  elif userSelection == 'q'
    break
  else
    print "Invalid selection"

