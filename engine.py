#!/usr/bin/env python

# The query file contains a query per line, "<Query #> <query tokens separated by spaces>"
# The docs file contains a doc description per line, "<Doc #> <doc tokens separated by spaces>"
class WordOverlap(object):
  def __init__(self):
    self._overlap_count = 0
    self._lines         = []
    
  def _getQueries(self):
    text = open('a2.qrys', 'r')
    self._lines = text.readlines()
    
  def count(self):
    self._getQueries()
    for line in self._lines:
      print line

def main():
  
  overlap = WordOverlap()
  overlap.count()
  
  print "Goodbye."

if __name__=="__main__":
  main()