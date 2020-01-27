from os import setpgrp
from subprocess import Popen
from time import sleep

# start jupyter notebook server on port 8086
Popen(
    ['nohup', 'jupyter', 'notebook', '--no-browser', '--port=8086'],
    stdout=open('nohup.out', 'w'),
    preexec_fn=setpgrp)

# wait for above process to finish
sleep(1)

# write jupyter server token to screen
token_file = open("nohup.out")

for line in token_file:
    if line.find("token=") > 0:
        print(line[line.find("token=")+6: ])
        break

token_file.close()






