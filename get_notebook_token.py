import subprocess
import os

subprocess.Popen(['nohup', 'jupyter', 'notebook', '--no-browser', '--port=8086'],
                 stdout=open('/dev/null', 'w'),
                 stderr=open('logfile.log', 'a'),
                 preexec_fn=os.setpgrp
                 )

token_file = open("nohup.out")

for line in token_file:
    if line.find("token=") > 0:
        print(line[line.find("token=")+6: ])
        break
