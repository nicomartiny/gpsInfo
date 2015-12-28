#transfer gps files to all other computers
import sys, os
from uuid import getnode as get_mac
import string



#try:
try:
	f = open('gpsCounter.txt', 'r')
except IOError:
	f = open('gpsCounter.txt', 'w+')
	


#f = open('gpsCounter.txt', 'r')
strCount = f.read()
#print(strCount)
if (strCount == ''):
	strCount = 0
	f = open('gpsCounter.txt', 'w')
	f.write('0')

	


#strGpsFileName = str(hex(get_mac()))[2:-1]
os.system("ifconfig eth0 | grep HWaddr |cut -dH -f2|cut -d\  -f2 >> ifConfigMacAddress.txt")
f = open("ifConfigMacAddress.txt")
strGpsFileName = f.read()
os.system("rm ifConfigMacAddress.txt")



strGpsFileName = strGpsFileName.replace(":", "_")
strGpsFileName = strGpsFileName.replace('\n', '')



newStrGpsFileName = ''


#for i in range(len(strGpsFileName)):
#	if(i % 2 == 0):
#		newStrGpsFileName = newStrGpsFileName + strGpsFileName[i:i+2] + '_'



#print(strGpsFileName)
newStrGpsFileName = strGpsFileName + '_' + str(strCount) + ".txt"	



listUser = []
listIp = []
listPassword = []

try:
	arpInfo = open('arpinfo.txt', 'r')
	for line in arpInfo:
		if (line.find("name:") > -1):
			listUser.append(line[line.index("name:") + 5:].replace('\n', ''))
		if (line.find("ip:") > -1):
			listIp.append(line[line.index("ip:") + 3:].replace("\n", ''))
		if (line.find("pass:") > -1):
			listPassword.append(line[line.index("pass:") + 5:].replace("\n", ''))

except IOError:
	print("Error: no init file")
#	os.system("nmap -sP 10.0.0.1/24")
#	os.system("nmap -sP 192.168.1.1/24")
#	os.system("arp -a >> arpinfo.txt")
#	arpInfo = open('arpinfo.txt' , 'r')
#	for line in arpInfo:
#		listUser.append(line[:line.index('.') - 8]  )
#		listIp.append(line[line.index('(') + 1:line.index(')')])





#print(listUser[0])
#print(listIp[0])


#strDestination = os.getcwd().split("magcarpc")


#listPassword = 'magadmin0229'


#Edit this command to have other computers info
for i in range(len(listUser)):
	osCommand =  'sshpass -p \"' + listPassword[i] +  '\"  scp -o StrictHostKeyChecking=no ' +  os.getcwd() + '/GPSResult/' + newStrGpsFileName  + ' '  + str(listUser[i]) + '@' + str(listIp[i]) +  ':/home/' + str(listUser[i]) + '/Desktop/WIFICapture/GPSResult/' + newStrGpsFileName


#print(osCommand)
os.system(osCommand)


f = open('gpsCounter.txt', 'w')
f.write(str(int(strCount) + 1))
