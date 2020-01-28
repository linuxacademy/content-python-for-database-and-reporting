import subprocess
import os
import time

subprocess.Popen(['nohup', 'jupyter', 'notebook', '--no-browser', '--port=8086'],
                 stdout=open('nohup.out', 'w'),
                 stderr=open('logfile.log', 'a'),
                 preexec_fn=os.setpgrp
                 )
time.sleep(1)
try:
    token_file = open("nohup.out")
except IOError:
    print("File not accessible")


for line in token_file:
    if line.find("token=") > 0:
        print(line[line.find("token=")+6: ])
        break
