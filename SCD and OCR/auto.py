import os
import argparse
import glob

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input video to extarct frames")

ap.add_argument("-t", "--thresh", default=5,
	help="threshold for delta_avg_hsv")

args = vars(ap.parse_args())

os.system("scenedetect -i "+args['input']+" -d content -s stats.csv -t "+args['thresh']+" -df 4 -co scenes.csv")

os.system("python scene_change_detector.py -i "+args['input'])

frames = [os.path.basename(i) for i in glob.glob("*.jpg")]

for frame in frames:
	os.system("python ocr.py -i "+frame+" > ocr_op"+frame[len(args['input'].split('.')[0]):-4]+".txt")


