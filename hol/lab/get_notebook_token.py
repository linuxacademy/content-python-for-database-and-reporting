import os
import psutil
from subprocess import Popen
from time import sleep

no_token = True

while no_token:
    # kill any jupyter notebook processes
    for proc in psutil.process_iter():
        if proc.name() == 'jupyter-noteboo':
            proc.kill()

    # delete old nohup.out if exists
    if os.path.exists("nohup.out"):
        os.remove("nohup.out")

    # start jupyter notebook server on port 8086
    Popen(
        ['nohup', 'jupyter', 'notebook', '--no-browser', '--port=8086'],
        stdout=open('nohup.out', 'w'),
        preexec_fn=os.setpgrp)

    # wait for above process to finish
    sleep(3)

    # write jupyter server token to screen
    token_file = open("nohup.out")

    for line in token_file:
        if line.find("token=") > 0:
            print(line[line.find("token=")+6: ])
            no_token = False
            break

    token_file.close()






