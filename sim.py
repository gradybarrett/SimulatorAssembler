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
    self.orig_imem = imem
    self.orig_dmem = dmem
    self.reset()

  def reset(self):
    """
    Reset all values as if starting from the beginning.
    """
    self.instruction_mem = self.orig_imem
    self.data_mem = self.orig_dmem
    
    self.running = True
    self.instr_counts = {"add":0, "sub":0, "load":0, "store":0, 
      "addi":0, "seti":0, "jump":0, "jz":0, "addptr":0, "subptr":0,
      "loadptr":0, "storeptr":0}
      
    self.reg_a = 0
    self.reg_b = 0
    self.reg_c = 0
    self.reg_d = 0
    self.reg_pc = 0

  def run(self):
    """
    Should execute all cycles until end of Imem
    """
    for instr in self.instruction_mem:
      print instr
      self.read_instr(instr)

  def step(self, numInstructions=1):
    """
    Given an integer representing the number of steps to be taken,
    step forward in the code
    """
    print self.instruction_mem[self.reg_pc]
    self.read_instr(self.instruction_mem[self.reg_pc])

  def restart(self, numInstruction=0):
    """
    Resets the simulation and steps defined number of Instructions
    """
    self.reset()
    self.step(numInstructions)

  def output_reg(self):
    """
    Outputs register values
    """
    print "a: " + str(self.reg_a)
    print "b: " + str(self.reg_b)
    print "c: " + str(self.reg_c)
    print "d: " + str(self.reg_d)
    print "pc: " + str(self.reg_pc)

  def output_dmem(self, index=None, mem_range=1):
    """
    Outputs data memory given starting index and mem_range
    """
    if index is None:
      index = 0
      mem_range = len(self.data_mem)

    while(mem_range > 0 and index < len(self.data_mem)):
      print str(self.data_mem[index]) 
      mem_range -= 1
      index += 1

  def output_imem(self, index=None, mem_range=1):
    """
    Outputs instruction memory given starting index and mem_range
    """
    if index is None:
      index = 0
      mem_range = len(self.instruction_mem)

    while(mem_range > 0 and index < len(self.instruction_mem)):
      i_string = str(self.instruction_mem[index][0]) + " " + str(self.instruction_mem[index][1])
      for i in range (2, 4, 1):
        if i < len(self.instruction_mem[index]):
          i_string += ", " + str(self.instruction_mem[index][i])
      print i_string
      mem_range -= 1
      index += 1
  
  def output_instr_cnt(self):
    for key, value in dict.items(self.instr_counts):
      print key.ljust(10), ":", value

  def read_instr(self, instr):
    """
    Look at location in imem and determine what we need to do
    Lots of cases (control)
    """
    if instr:
      self.reg_pc += 1
      if instr[0] == "add":
        setattr(self, 'reg_'+instr[1], getattr(self, 'reg_'+instr[1]) + self.data_mem[instr[2]])
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "sub":
        setattr(self, 'reg_'+instr[1], getattr(self, 'reg_'+instr[1]) - self.data_mem[instr[2]])
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "load":
        setattr(self, 'reg_'+instr[1], self.data_mem[instr[2]])
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "store":
        setattr(self, data_mem[instr[2]], getattr(self, 'reg_'+instr[1]))
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "addi":
        setattr(self, 'reg_'+instr[1], getattr(self, 'reg_'+instr[1]) + instr[2])
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "seti":
        setattr(self, 'reg_'+instr[1], instr[2])
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "jump":
        if self.reg_pc != instr[1]:
          self.reg_pc = instr[1]
        else:
          self.running = False
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "jz":
        if getattr(self, 'reg_'+instr[1]) is None:
          self.reg_pc = instr[2]
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "addptr":
        setattr(self, 'reg_'+instr[1], getattr(self, 'reg_'+instr[1]) + self.data_mem[getattr(self, 'reg_'+instr[2]) + instr[3]])
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "subptr":
        setattr(self, 'reg_'+instr[1], getattr(self, 'reg_'+instr[1]) - self.data_mem[getattr(self, 'reg_'+instr[2]) + instr[3]])
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "loadptr":
        setattr(self, 'reg_'+instr[1], self.data_mem[getattr(self, 'reg_'+instr[2]) + instr[3]])
        self.instr_counts[instr[0]] += 1
      elif instr[0] == "storeptr":
        self.data_mem[getattr(self, 'reg_'+instr[2]) + instr[3]] = getattr(self, 'reg_'+instr[1])
        self.instr_counts[instr[0]] += 1
