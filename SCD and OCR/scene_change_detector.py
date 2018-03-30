import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input video to extarct frames")

args = vars(ap.parse_args())

frame_nums = []
with open("scenes.csv") as fp:
    for i, line in enumerate(fp):
        if i >= 2:
            # read from 3rd line
            frame_nums.append(int(line.split(',')[1]))
print(frame_nums)

video_name = args['input']
cap = cv2.VideoCapture(video_name)
my_video_name = video_name.split(".")[0]
for frame_no in frame_nums:
	cap.set(1,frame_no)
	success,image = 	cap.read()
	cv2.imwrite(my_video_name+'_frame_'+str(frame_no)+'.jpg',image)	