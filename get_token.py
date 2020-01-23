token_file = open("nohup.out")

for line in token_file:
    if line.find("token=") > 0: 
        print(line[line.find("token=")+6: ])
        break
        


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


import subprocess
import os

# add mongodb repo and update with yum
subprocess.call(['sudo','mv', 'mongodb-org-4.0.repo', '/etc/yum.repos.d/'])
subprocess.call(['sudo', 'yum', 'update', '-y'])

# install mongdo, enable it and start it; adding the enable in case a student setsup their own server
subprocess.call(['sudo', 'yum', 'install', 'mongodb-org', '-y'])
subprocess.call(['sudo', 'systemctl', 'enable', 'mongod'])
subprocess.call(['sudo', 'systemctl', 'start', 'mongod'])

# install postgresql, create a db, enable it and start it 
subprocess.call(['sudo', 'yum', 'install', 'postgresql-server', 'postgresql-contrib', '-y'])
subprocess.call(['sudo', 'postgresql-setup', 'initdb'])
subprocess.call(['sudo', 'systemctl', 'enable', 'postgresql'])
subprocess.call(['sudo', 'systemctl', 'start', 'postgresql'])

# install python3 and virtualenv
subprocess.call(['sudo', 'yum', 'install', 'python3', '-y'])
subprocess.call(['pip3', 'install', '--user', 'virtualenv'])

# create python3 virtualenv and activate
subprocess.call(['mkdir', './venv'])
subprocess.call(['virtualenv', '-p', '/usr/bin/python3', 'python3'], cwd="./venv")
subprocess.call(['source', './python3/bin/activate'], cwd="./venv")

# upgrade pip3 and install jupyter notebook
subprocess.call(['python3', '-m', 'pip3', 'install', '--upgrade', 'pip'])
subprocess.call(['python3', '-m', 'pip3', 'install', 'notebook'])

# copy ipynb files to venv
# to do


# start jupyter notebook server on port 8086
subprocess.Popen(
                 ['nohup', 'jupyter', 'notebook', '--no-browser', '--port=8086'],
                 stdout=open('/dev/null', 'w'),
                 stderr=open('logfile.log', 'a'),
                 preexec_fn=os.setpgrp)

# write jupyter server token to screen
token_file = open("nohup.out")

for line in token_file:
    if line.find("token=") > 0:
        print(line[line.find("token=")+6: ])
        break

token_file.close()






