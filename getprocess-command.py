import subprocess;
process=subprocess.Popen(["powershell","gps | ? {$_.mainwindowtitle} | select name, mainwindowtitle | ft -AutoSize"],stdout=subprocess.PIPE);
result=process.communicate()[0]
import re
c=result.decode('ascii').strip()
# print(c)
f = []
f=c.split('\r\n')
for ii in f:
    s = re.sub(' +', ' ', ii)
    print(s)
    value = re.split('(\d+)', s)
    value[0] = re.sub(' ', '', value[0])
    s = re.sub(' ', '', value[0])
    # print(value)
    # print(filter(None, re.split(r'(\d+)', s)))
s=[]
