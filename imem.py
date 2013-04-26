#!/usr/bin/env python

import fileinput
import re

class Instr_Mem(object):

  def __init__(self, filename):
    self.fn = filename
    self.instruction_memory = []
    self.parse()

  def parse(self):
    for line in fileinput.input(self.fn):
      result =  re.match(r'([a-z]*) ([abcd]), (([abcd]), ([0-9])|([0-9]*))', line)
      if result:
        if result.group(6):
          self.instruction_memory.append([result.group(1),result.group(2),int(result.group(6))])
        if result.group(4):
          self.instruction_memory.append([result.group(1),result.group(2),result.group(4),int(result.group(5))])

  def output_array(self):
    return self.instruction_memory
