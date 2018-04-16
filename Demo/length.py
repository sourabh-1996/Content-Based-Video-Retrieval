import MapReduce
import sys
from collections import *
from math import *


mr = MapReduce.MapReduce()


def mapper(record):

    word = record[0]
    count = record[1]
    docs = record[2]
    for x in docs:
        mr.emit_intermediate(x[0], x[1])
        #print x

def reducer(key, list_of_values):

    sum = 0
    for x in list_of_values:
        square = x**2
        sum = sum + square
    length = sqrt(sum)    
    mr.emit((key, length))


apple = []
if __name__ == '__main__': 
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  
  
