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
      result =  re.match(r'([a-z]*) ([abcd]), (([abcd]), ([0-9])|([0-9]*))', line)
      if result:
        if result.group(6):
          self.instruction_memory.append([result.group(1),result.group(2),int(result.group(6))])
        if result.group(4):
          self.instruction_memory.append([result.group(1),result.group(2),result.group(4),int(result.group(5))])

  def output_array(self):
    return self.instruction_memory
