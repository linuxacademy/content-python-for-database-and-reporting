import subprocess
import os

# start jupyter notebook server on port 8086
subprocess.Popen(
                 ['nohup', 'jupyter', 'notebook', '--no-browser', '--port=8086'],
                 stdout=open('nohup.out', 'w'),
                 stderr=open('logfile.log', 'a'),
                 preexec_fn=os.setpgrp)

# write jupyter server token to screen
token_file = open("nohup.out")

for line in token_file:
    if line.find("token=") > 0:
        print(line[line.find("token=")+6: ])
        break

token_file.close()






