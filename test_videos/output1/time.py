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
if("output"+n+".txt" in ls):
	ls.remove("output"+n+".txt")
ls.sort(key=natural_keys)
print(ls)
f = open("output"+n+".txt","w")
time=0
for file in ls:
	f1 = open(file,"r")
	print(file,time)
	for line in f1:
		if(line[0]=="W"):
			ls2 = line[6:].split(",")
			f.write(ls2[0]+" "+"Start Time:"+str((time+float(ls2[1][13:]),1))+", End time:"+ str(round(time+float(ls2[2][11:]),1)))
			f.write("\n");
	time = time+49.9
	print(file,time);
	f1.close()	