import sys
import json
from collections import *
from math import *
import operator
import os

length_vectors = {}                     

cosine_similarity = {}
doc_lengths = open("vector_lengths.txt")
for line in doc_lengths:
    data = json.loads(line)
    doc_id = data[0]
    length = data[1]
    length_vectors[doc_id] = length
    cosine_similarity[doc_id] = 0




Index = {}

inverted_index = open("index.txt")
for line in inverted_index:
    data = json.loads(line)
    word =  data[0]
    count = data[1]
    docs = data[2]
    Index[word] = docs


def relevance(query):
    similarity = {}
    query_vector = query.split(' ')
    for x in query_vector:
        relevant_docs = Index[x]
        for d in relevant_docs:
            document = d[0]
            score = d[1]
            cosine_similarity[document] = cosine_similarity[document] + score
    for y in cosine_similarity.keys():
        cosine_similarity[y] = float(cosine_similarity[y])/float(len(query_vector)*length_vectors[y])
    sorted_similarity = sorted(cosine_similarity.items(), key=operator.itemgetter(1), reverse=True)    
    return sorted_similarity

def convert_to_min(sec):
    sec = float(sec)
    mini = int(sec//60)
    time = int(sec%60)
    stri=str(mini)+":"+str(time)
    return stri    

search_query = sys.argv[1]
a = relevance(search_query)
print(a)
print("\n\n")
for i in a:
    doc = i[0]
    os.chdir("Timestamps")
    with open (doc, 'rb') as input:
        content = input.readlines()
        ls=[]
        for line in content:
            line = line.decode("utf-8")
            line_arr = line.split(" ")
            if(line_arr[0] == search_query):
                t = line_arr[2]
                s = t.find("(")
                e = t.find(",")
                sub = t[s+1:e]
                sub = convert_to_min(sub)
                ls.append(sub)
        if(ls!=[]):
            print("Results from: "+doc)
            print(ls)        
    os.chdir("..")




