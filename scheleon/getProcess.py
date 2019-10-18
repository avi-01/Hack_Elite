import subprocess
import re
import requests
import json

allowedProcesses = []
file = open("allowedProcesses.txt", "r")
for name in file:
	name = re.sub('\n', '', name)
	allowedProcesses.append(name)
print(allowedProcesses)

processNameSource = subprocess.Popen(["powershell","gps | ? {$_.mainwindowtitle} | select name | ft -AutoSize"],stdout=subprocess.PIPE);
processMainWindowTitleSource = subprocess.Popen(["powershell","gps | ? {$_.mainwindowtitle} | mainwindowtitle | ft -AutoSize"],stdout=subprocess.PIPE);

processNames = processNameSoucre.communicate()[0].decode('ascii').strip().split('\r\n')
processMainWindowTitles = processMainWindowTitles.communicate()[0].decode('ascii').strip().split('\r\n')

# removed Column titles : 'Names' from the list
del processNames[0-2]
del processMainWindowTitles[0-2]

for ii in range(0, len(processNames) - 1) :
    processNames[ii] = re.sub(' +', '', processNames[ii])
    
for ii in range(0, len(processMainWindowTitles) - 1) :
    processMainWindowTitles[ii] = re.sub(' +', '', processMainWindowTitles[ii])

processesToCLose = []
for ii in range(0, len(processNames)-1) :
	runningProcess = []
	runningProcess.append(processNames[ii])
	runningProcess.append(processMainWindowTitles[ii])
	result = [allowedProcessName for allowedProcessName in allowedProcesses if(allowedProcessName.lower() in runningProcess[0].lower() or runningProcess[0].lower() in allowedProcessName.lower())]
	if not bool(result) :
		processesToCLose.append(runningProcess);

jsonStringProcessesToClose = json.dumps(processesToCLose, separators=(',', ':'));

if bool(processesToCLose)
	requests.post(url = "http://localhost:3001", jsonStringProcessesToClose)