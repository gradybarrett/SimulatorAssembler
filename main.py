#!/usr/bin/env python

from imem import Instr_Mem
from dmem import Data_Mem
from sim import Simulator

imem = Instr_Mem("imem.txt")
dmem = Data_Mem("dmem.txt")
prog1 = Simulator(imem.output_array(), dmem.output_array())
prog1.step()
prog1.read_values()
prog1.step()
prog1.read_values()
prog1.step()
prog1.read_values()
prog1.step()
prog1.read_values()
prog1.step()
prog1.read_values()
