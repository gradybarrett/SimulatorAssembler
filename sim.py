#!/usr/bin/env python

import os

class Simulator(object):
  """
  Our SM16 Simulator
  """

  def __init__(self, imem, dmem):
    """
    Initialize the Simulator and specify verbosity
    """
    self.instruction_mem = imem
    self.data_mem = dmem

    self.reg_a = 0
    self.reg_b = 0
    self.reg_c = 0
    self.reg_d = 0
    self.reg_pc = 0

  def run(self):
    """
    Should execute all cycles until end of Imem
    """

  def step(self, numInstructions=1):
    """
    Given an integer representing the number of steps to be taken,
    step forward in the code
    """

  def read_values(self):
    """
    Outputs register values
    """

  def read_instr(self):
    """
    Look at location in imem and determine what we need to do
    Lots of cases (control)
    """
    for instr in self.instruction_mem:
      if instr[0] == "add":
        vars()["reg_"+instr[1]] = vars()["reg_"+instr[1]] + dmem[instr[2]]
      elif instr[0] == "sub":
        vars()["reg_"+instr[1]] = vars()["reg_"+instr[1]] - dmem[instr[2]]
        elif instr[0] == "load":
            vars()["reg_"+instr[1]] = dmem[instr[2]]
        elif instr[0] == "store":
            dmem[instr[2]] = vars()["reg_"+instr[1]]
        elif instr[0] == "addi":
            vars()["reg_"+instr[1]] = vars()["reg_"+instr[2]] + instr[3]
        elif instr[0] == "seti":
            vars()["reg_"+instr[1]] = instr[2]
        elif instr[0] == "jump":
            reg_pc = instr[1]
        elif instr[0] == "jz":
            if vars()["reg_"+instr[1]] == None:
                reg_pc = instr[2]
            reg_pc += 1
        elif instr[0] == "addptr":
            vars()["reg_"+instr[1]] = vars()["reg_"+instr[1]] + dmem[vars()["reg_"+instr[2]]+ instr[3]]
        elif instr[0] == "subptr":
            vars()["reg_"+instr[1]] = vars()["reg_"+instr[1]] - dmem[vars()["reg_"+instr[2]]+ instr[3]]
        elif instr[0] == "loadptr":
            vars()["reg_"+instr[1]] = dmem[vars()["reg_"+instr[2]]+ instr[3]]
        elif instr[0] == "storeptr":
            dmem[vars()["reg_"+instr[2]]+ instr[3]] = vars()["reg_"+instr[1]]
        else:
            reg_pc += 1
