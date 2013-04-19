#!/usr/bin/env python

from imem import Instr_Mem
from dmem import Data_Mem
from sim import Simulator

imem = Instr_Mem("imem.txt")
dmem = Data_Mem("dmem.txt")
Simulator(imem, dmem)
