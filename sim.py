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
    print self.instruction_mem[self.reg_pc]
    self.read_instr(self.instruction_mem[self.reg_pc])

  def read_values(self):
    """
    Outputs register values
    """
    print "a: " + str(self.reg_a)
    print "b: " + str(self.reg_b)
    print "c: " + str(self.reg_c)
    print "d: " + str(self.reg_d)
    print "pc: " + str(self.reg_pc)

  def read_instr(self, instr):
    """
    Look at location in imem and determine what we need to do
    Lots of cases (control)
    """
    if instr:
      self.reg_pc += 1
      if instr[0] == "add":
        setattr(self, 'reg_'+instr[1], getattr(self, 'reg_'+instr[1]) + self.data_mem[instr[2]])
      elif instr[0] == "sub":
        setattr(self, 'reg_'+instr[1], getattr(self, 'reg_'+instr[1]) - self.data_mem[instr[2]])
      elif instr[0] == "load":
        setattr(self, 'reg_'+instr[1], self.data_mem[instr[2]])
      elif instr[0] == "store":
        setattr(self, data_mem[instr[2]], getattr(self, 'reg_'+instr[1]))
      elif instr[0] == "addi":
        setattr(self, 'reg_'+instr[1], getattr(self, 'reg_'+instr[1]) + instr[2])
      elif instr[0] == "seti":
        setattr(self, 'reg_'+instr[1], instr[2])
      elif instr[0] == "jump":
        self.reg_pc = instr[1]
      elif instr[0] == "jz":
        if getattr(self, 'reg_'+instr[1]) is None:
          self.reg_pc = instr[2]
      elif instr[0] == "addptr":
        setattr(self, 'reg_'+instr[1], getattr(self, 'reg_'+instr[1]) + self.data_mem[getattr(self, 'reg_'+instr[2]) + instr[3]])
      elif instr[0] == "subptr":
        setattr(self, 'reg_'+instr[1], getattr(self, 'reg_'+instr[1]) - self.data_mem[getattr(self, 'reg_'+instr[2]) + instr[3]])
      elif instr[0] == "loadptr":
        setattr(self, 'reg_'+instr[1], self.data_mem[getattr(self, 'reg_'+instr[2])] + instr[3])
      elif instr[0] == "storeptr":
        #TODO wasnt sure on this
        dmem[vars()["reg_"+instr[2]]+ instr[3]] = vars()["reg_"+instr[1]]
