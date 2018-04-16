import os
import glob
import moviepy.editor as mp
os.chdir("test_videos")

i=1
for file in glob.glob("*.mp4"):
	clip = mp.VideoFileClip(file)
	clip.audio.write_audiofile("audio"+str(i)+".mp3")
	i=i+1
j=1
for file in glob.glob("*.mp3"):
	if not os.path.exists("output"+str(j)):
		os.makedirs("output"+str(j))
	os.system("ffmpeg -i "+file+" -f segment -segment_time 50 -c copy output"+str(j)+"/out%01d.wav")
	j = j+1

k=1
for file in glob.glob("output*"):
	os.chdir(file)
	for file1 in glob.glob("*.wav"):
		os.system("ffmpeg -i "+file1+" -ac 1 out"+str(k)+".flac")
		#print(file1,k)
		k=k+1
	k=1
	