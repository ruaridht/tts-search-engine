#!/usr/bin/env python

import re

# The query file contains a query per line, "<Query #> <query tokens separated by spaces>"
# The docs file contains a doc description per line, "<Doc #> <doc tokens separated by spaces>"
class WordOverlap(object):
  def __init__(self):
    self._queries      = []
    self._documents	   = []
    self._performWrite = False
    self.freqs         = []
    
  def _getQueries(self):
    text = open('a2.qrys', 'r')
    self._queries = text.readlines()
    
  def _getDocuments(self):
    text = open('a2.docs', 'r')
    self._documents = text.readlines()
    
  def _getWords(self, query):
    q = re.sub(r"(?<=[a-z])\r?\n","", query)
    words = q.split(' ')
    #words = words[2:]
    return words
    
  def _writeOut(self, freqs):
    f = open('overlap.top','w')
    for query in freqs:
      for count in query:
        output = count[0] + " 0 " + count[1] + " 0 " + count[2] + " 0 \n"
        f.write(output)
    f.close()
  
  def _overlap(self):
    freq = []
    docs = []
    qrys = []
    
    query_freq = []
    
    for doc in self._documents:
      d_words = self._getWords(doc)
      docs.append(d_words)
      
    for query in self._queries:
      q_words = self._getWords(query)
      qrys.append(q_words)
      
    for query in qrys:
      word_freq_for_query = []
      # NOTE: Working with only the first 10 docs!!
      for doc in docs:
        word_count = 0
        for word in query[2:]:
          if word in doc:
            word_count += 1
        # Exclude documents with a count of 0
        if (word_count > 0):
          # Store the word count and the document number
          word_freq_for_query.append((query[0],doc[0],str(word_count)))
      query_freq.append(word_freq_for_query)
    
    """
    for query in query_freq:
      for query_count in query:
        print query_count[0] + " 0 " + query_count[1] + " 0 " + query_count[2] + " 0 "
    """
    
    if (self._performWrite):
      # Write the results to file
      self._writeOut(query_freq)
      print ">>> Writing word overlaps to overlap.top."
    self.freqs = query_freq
       
  
  def count(self, write):
    self._performWrite = write
    self._getQueries()
    self._getDocuments()
    self._overlap() 

def main():
  
  # 'write' determines whether we write to file or not.
  overlap = WordOverlap()
  overlap.count(write=True)
  
  #tf = Tfidf(overlap.freqs)
  #tf.retrieve(write=False)
  
  print "Done! Goodbye."

if __name__=="__main__":
  main()