#!/usr/bin/env python

import re
import math
import porter2

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
    
# tf.idf class
class Tfidf(object):
  def __init__(self, o_docs, o_queries):
    self._performWrite  = False
    self._documents     = o_docs
    self._queries       = o_queries
    self._dWords        = []
    self._qWords        = []
    self._weighted_sums = []
    
  def _writeOut(self):
    f = open('tfidf.top','w')
    for query in self._weighted_sums:
      for weight in query:
        f.write(weight[0] + " 0 " + weight[1] + " 0 " + weight[2] + " 0 \n")
    f.close()
    
  def _parseWords(self):
    for doc in self._documents:
      self._dWords.append(doc.split())
    for qry in self._queries:
      self._qWords.append(qry.split())
  
  def _numDocsContain(self, w):
    num = 0
    for doc in self._documents:
      if w in doc:
        num += 1
    return num
    
  def _stemStopwordDocs(self):
    
  
  def _sum(self):
    k            = 2.0
    weighted_sum = 0.0
    num_docs     = len(self._dWords)
    doc_len_avg  = 0.0
    
    for doc in self._dWords:
      doc_len_avg += len(doc)-1.0 # Subtract 1 to 
    doc_len_avg = doc_len_avg / len(self._dWords) # The averaging step
    
    # The main tf.idf loop
    # For each query we calculate the tf.idf for each document and add this to the list.
    # This means query_weights will be len(documents) and weighted sums will be len(queries)
    # and the overall size will be len(queries)*len(documents) ?
    for query in self._qWords:
      query_weights = []
      print "Query " + query[0]
      
      for doc in self._dWords:
        doc_len = len(doc)-1.0
        weighted_sum = 0.0
        
        for word in query[1:]:
          word = porter2.stem(word)
          tf_wq = query.count(word)
          tf_wd = doc.count(word)
          df_w  = 0.0
          tf_idf = 0.0
          # No point calculating the tf.idf if we know it's going to be zero
          if (tf_wd != 0):
            df_w = self._numDocsContain(word) # This step takes ages. :(
            tf_idf = (tf_wq*(tf_wd / (tf_wd + ((k*doc_len)/doc_len_avg) ))*(math.log(num_docs/df_w, math.e)))
          weighted_sum += tf_idf
          
        # Only care about things with a weight above 0
        if (weighted_sum != 0):
          query_weights.append((query[0], doc[0], str(weighted_sum)))
      
      self._weighted_sums.append(query_weights)
      
    if (self._performWrite):
      self._writeOut()
    
  def _stem(self):
    for query in self._qWords:
      for word in query:
        print word, porter2.stem(word)
      break
    
  def retrieve(self, write):
    self._performWrite = write
    self._parseWords()
    self._sum()
    #self._stem()

def main():
  # The query file contains a query per line, "<Query #> <query tokens separated by spaces>"
  # The docs file contains a doc description per line, "<Doc #> <doc tokens separated by spaces>"
  
  # 'write' determines whether we write to file or not.
  
  # Get the word overlap count.  Here we are counting how many of the query words appear in
  # the document, rather than how many times the query words appear (equation description delcares
  # binary weighting)
  overlap = WordOverlap()
  overlap.count(write=False)
  
  # Compute the tf.idf weighted sum
  tf = Tfidf(overlap._documents,overlap._queries)
  tf.retrieve(write=True)
  
  
  print "Done! Goodbye."

if __name__=="__main__":
  main()