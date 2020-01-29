# Creating Your Playground Server

 It is advised your start a Playground server to follow along with the lessons and practice on your own.

## Create a Playground server

We are going to create a simple Centos7 server and install what we need as we go along.  Choosing **`Centos 7`** will install a basic Centos 7 server.

### Playground Server Settings

Choose the following settings in making your Playground Server. **_You may choose a different tag if desired._**

- Distribution: Ubuntu 18.04 Bionic Beaver LTS
- Zone: North America
- Size: Micro
- Tag: Using Python for Database Operations and Reporting

## SSH into your playground server

Once the server indicates it is ready, using your terminal:

``` bash
ssh cloud_user@<the public IP address shown>
```

- type **`yes`** when asked to allow connection to the server
- enter **`<the temporary password shown>`**
- You will be asked to change your password
- For Old Password, enter **`<the temporary password shown>`**
- For New Password, enter **`your new password`**
- Enter the New Password again, enter **`your new password`**
- **Don't forget your new password!**  You will use this new password when you log-in to your Playground server.

## Update Ubuntu

Let's make sure we have all security patches installed on the server:

``` bash
  sudo apt update && sudo apt upgrade -y
```

texlive-xetex


## Installing Anaconda
cd /tmp
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh

sha256sum Anaconda3-2019.03-Linux-x86_64.sh
  45c851b7497cc14d5ca060064394569f724b67d9b5f98a926ed49b834a6bb73a  Anaconda3-2019.03-Linux-x86_64.sh

bash Anaconda3-2019.03-Linux-x86_64.sh


Welcome to Anaconda3 2019.03

In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>>
...
Do you approve the license terms? [yes|no]

Output
Anaconda3 will now be installed into this location:
/home/sammy/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/sammy/anaconda3] >>>

Output
...
installation finished.
Do you wish the installer to prepend the Anaconda3 install location
to PATH in your /home/sammy/.bashrc ? [yes|no]
[no] >>> 

cd ~conda 
source ~/.bashrc

conda config --set auto_activate_base false
conda update -n base -c defaults conda

conda create -n python_data_course python=3

## Use the git Repo for the Course to Practice What We Do in Lessons

Now we will make a directory to hold our work and virtual envrionment.

``` bash
mkdir python_for_database_reporting
```

**You change the above name to something you like if desired.**

``` bash
cd python_for_database_reporting
```

conda activate python_data_course
conda install jupyter psutil


Now we need to clone the git repo for the course

``` bash  
git clone https://github.com/linuxacademy/content-python-for-database-and-reporting.git .
```



## Connecting to the Jupyter Notebook Server

### On the Playground Server

**Make sure that you have activated the virtual environment!**

To activate the virtual environment:

``` bash
cd /home/cloud_user/python_for_database_reporting
```

``` bash
pipenv shell
```

To start the server run the following:

``` bash
python get_notebook_token.py
```

_This is a simple script that starts the jupyter notebook server and sets it to continue to run outside of the terminal:_

_```nohup jupyter notebook --no-browser --port=8088```_

_It then searches the resulting text file `nohup.out` to find and print the token._

**On the terminal is a token, you must copy this and save it to a text file on your local machine.**

### On Your Local Machine

In a terminal window enter the following:

``` bash
ssh -N -L localhost:8088:localhost:8088 cloud_user@<the public IP address of the Playground server>
```

_-N indicates that there will be no remote commands_
_-L maps the local port to the remote port

**Leave this terminal open, it will appear nothing has happened, but it must remain open while you use the Jupyter Notebook server in this session.**

In the browser of your choice enter the following address:

**```http://localhost:8088```**

This will open a Jupyter Notebook site that asks for the token you copied from the remote server.
