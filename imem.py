#!/usr/bin/env python

import fileinput
import re

class Instr_Mem(object):

  def __init__(self, filename):
    self.fn = filename
    self.vhdl_output = open('instruction_memory.vhdl', 'w')
    self.instruction_memory = []
    self.instr_binary = {"add":"0000", "sub":"0001", "load":"0010", "store":"0011", 
      "addi":"0100", "seti":"0101", "jump":"0110", "jz":"0111", "addptr":"1000", "subptr":"1001",
      "loadptr":"1010", "storeptr":"1011", 'a':"00", 'b':"01", 'c':"10", 'd':"11"}
    self.parse()

  def parse(self):
    instr_count = 0
    for line in fileinput.input(self.fn):
      jtype = re.match(r'([a-z]+) ([0-9]+)', line)
      btype = re.match(r'([a-z]+) ([abcd]), ([0-9]+)', line)
      ptype = re.match(r'([a-z]+) ([abcd]), ([abcd]), ([0-9]+)', line)
      if jtype:
        self.instruction_memory.append(jtype.groups())
        self.write_to_vhdl_file('j', instr_count, jtype.groups())
      elif btype:
        self.instruction_memory.append(btype.groups())
        self.write_to_vhdl_file('b', instr_count, btype.groups())
      elif ptype:
        self.instruction_memory.append(ptype.groups())
        self.write_to_vhdl_file('p', instr_count, ptype.groups())
      instr_count += 1
    self.vhdl_output.close()

  def write_to_vhdl_file(self, type, count, output):
    if type == 'j':
      self.vhdl_output.write(
        "\""+self.instr_binary[output[0]]+
        bin(int(output[1]))[2:].zfill(12)+"\""+
        "  -- "+str(count)+": "+" ".join(output)+"\n")
    elif type == 'b':
      self.vhdl_output.write(
        "\""+self.instr_binary[output[0]]+
        self.instr_binary[output[1]]+
        bin(int(output[2]))[2:].zfill(10)+"\""+
        "  -- "+str(count)+": "+" ".join(output)+"\n")
    elif type == 'p':
      self.vhdl_output.write(
        "\""+self.instr_binary[output[0]]+
        self.instr_binary[output[1]]+
        self.instr_binary[output[2]]+
        bin(int(output[3]))[2:].zfill(8)+"\""+
        "  -- "+str(count)+": "+" ".join(output)+"\n")
  
  def output_array(self):
    return self.instruction_memory
