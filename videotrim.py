import sys
import os
import subprocess

def hmsToSec(hms):
	#Works for HH:MM:SS and MM:SS
	split = hms.split(":")
	rate = 1
	total = 0
	for part in reversed(split):
		total = total + rate * int(part)
		rate = rate * 60
	return total

def main(argv):
	video = ""
	if len(argv) == 0:
		print "Error: Please choose a video"
		return
	else:
		video = argv[0]
	
	start = False
	end = False
	
	if len(argv) == 3:
		start = hmsToSec(argv[1])
		end = hmsToSec(argv[2])
	else:
		start = raw_input("Enter Start Time (HH:MM:SS): ")
		end = raw_input("Enter End Time (HH:MM:SS): ")
		start = hmsToSec(start)
		end = hmsToSec(end)
	vid = os.path.split(video)[1]
	vi = os.path.splitext(vid)
	
	filename = vi[0] + "-trimmed.ts"
	i = 1
	while os.path.exists(filename) and os.path.isfile(filename):
		filename = vi[0] + "-trimmed-" + str(i) + vi[1]
		i = i + 1
	
	subprocess.call(["ffmpeg/bin/ffmpeg.exe", "-i", video, "-ss", str(start), "-c", "copy", "-t", str(end-start), filename])

if __name__ == "__main__":
	main(sys.argv[1:])