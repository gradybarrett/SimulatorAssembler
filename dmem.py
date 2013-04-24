#!/usr/bin/env python

import fileinput
import re

class Data_Mem(object):

  def __init__(self, filename):
    self.fn = filename
    self.data_memory = []
    self.parse()

  def parse(self):
    for line in fileinput.input(self.fn):
      result = re.match(r'([0-9]*)', line)
      if result:
        self.data_memory.append(result.group(1))

  def output_array(self):
    return self.data_memory
