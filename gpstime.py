import datetime
import os,sys
import time

while(True):
	os.system("gpspipe -n 5 -w -o gpstime.txt")
	f = open("gpstime.txt", "r")
	for line in f:
		if line.find("time") > -1:
			if line.find("lat") > -1:
				if float(line[line.index("lat") + 5: line.index("lat") + 14]) > 20.5:
					if float(line[line.index("lat") + 5: line.index("lat") + 14]) < 48:
						strTime = "date -s " + line[line.index("time") + 7: line.index("time") + 31]
#						print(strTime)
						os.system(strTime)

	time.sleep(10)
