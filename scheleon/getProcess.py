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

processNameSource = subprocess.Popen(["powershell","gps | ? {$_.mainwindowtitle} | select name | ft -AutoSize"],stdout=subprocess.PIPE)

processNames = processNameSource.communicate()[0].decode('ascii').strip().split('\r\n')

for ii in range(0, len(processNames) - 1) :
    processNames[ii] = re.sub(' +', '', processNames[ii])
    
# removed Column titles : 'Names' from the list
del processNames[:2]

processesToCLose = []
for ii in range(0, len(processNames)-1) :
	runningProcess = processNames[ii]
	result = [allowedProcessName for allowedProcessName in allowedProcesses if(allowedProcessName.lower() in runningProcess.lower() or runningProcess.lower() in allowedProcessName.lower())]
	if not bool(result) :
	    processesToCLose.append(runningProcess)

jsonStringProcessesToClose = json.dumps(processesToCLose, separators=(',', ':'))
print(jsonStringProcessesToClose)

if bool(processesToCLose) :
    requests.post(url = "http://localhost:3001", jsonStringProcessesToClose)
