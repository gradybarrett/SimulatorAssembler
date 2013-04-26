#!/usr/bin/env python

import fileinput
import re

class Instr_Mem(object):

  def __init__(self, filename):
    self.fn = filename
    self.instruction_memory = []
    self.parse()
    self.instr_counts = {"add":"0000", "sub":"0001", "load":"0010", "store":"0011", 
      "addi":"0100", "seti":"0101", "jump":"0110", "jz":"0111", "addptr":"1000", "subptr":"1001",
      "loadptr":"1010", "storeptr":"1011", 'a':"00", 'b':"01", 'c':"10", 'd':"11"}

  def parse(self):
    for line in fileinput.input(self.fn):
      jtype = re.match(r'([a-z]+) ([0-9]+)', line)
      btype = re.match(r'([a-z]+) ([abcd]), ([0-9]+)', line)
      ptype = re.match(r'([a-z]+) ([abcd]), ([abcd]), ([0-9]+)', line)
      if jtype:
        self.instruction_memory.append(jtype.groups())
      elif btype:
        self.instruction_memory.append(btype.groups())
      elif ptype:
        self.instruction_memory.append(ptype.groups())

  def output_array(self):
    return self.instruction_memory
