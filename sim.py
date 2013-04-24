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
