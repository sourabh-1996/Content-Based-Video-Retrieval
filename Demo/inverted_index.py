import MapReduce
import sys
from collections import *
from math import *



mr = MapReduce.MapReduce()

# =============================
number_of_documents = 10

def mapper(record):
    key = record[0]
    value = record[1]
    max_freq = 0
    word_freq = defaultdict(int)
    words = value.split()
    for w in words:
        word_freq[w] = word_freq[w] + 1  
    '''    
    for w in words:
        if (word_freq[w] > max_freq):
            max_freq = word_freq[w]
        else:
            max_freq = max_freq
    #print max_freq
    '''
    for w in words:
        #tf_norm = float(word_freq[w])/float(max_freq)
        tf_norm = 1+log(word_freq[w],2)
        mr.emit_intermediate(w,[key, tf_norm])

def reducer(key, list_of_values):

    index = []
    count = 0
    for x in list_of_values:
        if not(x in index):
            index.append(x)
            count =  count + 1
    df = float(number_of_documents)/float(count)        
    idf = log(df, 2) 
    for y in index:
        y[1] = y[1]*idf
    mr.emit((key,count, index))
    
if __name__ == '__main__':  
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  
  
