#!/usr/bin/env python

import fileinput

class Data_Mem(object):

  def __init__(self, filename):
    self.fn = filename
    self.parse()

  def parse(self):
    for line in fileinput.input(self.fn):
      #TODO parse datamem
