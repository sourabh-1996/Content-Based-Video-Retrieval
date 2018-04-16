import glob
import os
import shutil
'''
for file2 in glob.glob("output*"):
		shutil.copy2("s2t.py",file2)
'''
for file2 in glob.glob("*.flac"):
	b = file2.split(".")
	c = b[0][3:]
	os.system("python s2t.py "+file2+" >>"+c+".txt")
