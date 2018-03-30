import os
import glob
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

n = os.getcwd()[-1]
ls=[]
for file in glob.glob("*.txt"):
	ls.append(file)
if("output"+n+"_text.txt" in ls):
	ls.remove("output"+n+"_text.txt")
ls.sort(key=natural_keys)
print(ls)
f = open("output"+n+"_text.txt","w")
for file in ls:
	f1 = open(file,"r")
	for line in f1:
		if(line[0:11]=="Transcript:"):
			f.write(line[12:-1])
			f.write("\n")
	f1.close()
