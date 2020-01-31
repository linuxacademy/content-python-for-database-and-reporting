# Creating Your Playground Server

 It is advised your start a Playground server to follow along with the lessons and practice on your own.

## Create a Playground server

We are going to create a simple Centos7 server and install what we need as we go along.  Choosing **`Ubuntu 18.10 Bionic Beaver LTS`** will install a basic Ubuntu 18 server.

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

During this process an information screen will pop up that looks like this:

![alt text](https://github.com/linuxacademy/content-python-for-database-and-reporting/blob/master/data/screenshots/screenshot_grub_ok.png?raw=true)

Just select `enter` or `return`.

Then another information screen will pop up that looks like this:

![alt text](https://github.com/linuxacademy/content-python-for-database-and-reporting/blob/master/data/screenshots/screenshot_grub_selection.png?raw=true)

Now select `space` and then `return/enter`.

We need to install one more package needed for our work.  This package is needed to later turn our notebooks to PDF.

``` bash
sudo apt install -y texlive-xetex
```

## Installing Anaconda

We are using [Anaconda](https://www.anaconda.com/) for this course.  Anaconda is a data science and machine learning platform based on Python that can also be used to write standard Python apps also.  We will be using it because it makes the use of Jupyter Notebooks very easy.  The work with the Jupyter Notebooks could be done without it but it suggested by [Project Jupyter](https://jupyter.org/) that using Anaconda is the best solution.

To install, we first need to download the Anaconda package

``` bash
cd /tmp
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
```

We should check that the package we downloaded is not corrupt:

``` bash
  sha256sum Anaconda3-2019.03-Linux-x86_64.sh
```

The result should be:

- 45c851b7497cc14d5ca060064394569f724b67d9b5f98a926ed49b834a6bb73a  Anaconda3-2019.03-Linux-x86_64.sh

If the checksum is not the same, if the checksums do not match, it indicates the file may be corrput in some way.  **Please stop installation of the Playground server.** **_Please ask for help from Linux Academy before proceeding._**

If the checksums do match being the installation of Anaconda:

``` bash
bash Anaconda3-2019.03-Linux-x86_64.sh
```
Near the beginning of the install you will get this message:

``` text
Welcome to Anaconda3 2019.03

In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>>
```

After reading the license agreement, you will get the message:

``` text
Do you approve the license terms? [yes|no]
```

if you enter `yes` then this message will appear:

``` text
Anaconda3 will now be installed into this location:
/home/sammy/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/sammy/anaconda3] >>>
```

Please make the appropriate selection.

After installation is complete, this message will appear:

``` text
installation finished.
Do you wish the installer to prepend the Anaconda3 install location
to PATH in your /home/sammy/.bashrc ? [yes|no]
[no] >>> 
```

Please enter ```yes```.  This will update you ~/.bashrc file so that you can use `conda` on the command.

Move back to your directory:

``` bash
cd ~
```

We need to restart the shell to include the changes made:

``` bash
source ~/.bashrc
```

You will see a `(base)` prepended to your command line.  That indicates that the base conda virtual environment has been activated.  This will happen everytime we start the terminal.  We don't want that behavior; to turn it off:

``` bash
conda config --set auto_activate_base false
```

Now let's update the conda base code:

``` bash
conda update -n base -c defaults conda
```

## Create a conda Environment For This Course

We want to create a conda virtual environment for this course using Python 3.  I am naming this environment `python_data_course` using the `-n` flag.  You may choose a different virtual envornment name.  `python=3` tells the virtual environment to use the lastest version of Python 3 installed in conda.

``` bash
conda create -n python_data_course python=3
```

You will need to activate this virtual environment before you work on the code in the repo we are about to clone.  To do so:

``` bash
conda activate python_data_course
```

To leave the virtual environment:

``` bash
conda deactivate
```

**Please note: You will recieve errors if you try to run the code without activated the virtual environment.  If you do encounter errors when starting work, please check that you have activated the virtual environment.**


## Use the git Repo for the Course to Practice What We Do in Lessons


Now we will make a directory to hold the github repo.

``` bash
mkdir python_data_course
```

**You change the above name to something you like if desired.**

Move to the directory, activate the virtual environment (if it is not active, look for the parenthesis statement prepended to your command line, it does not hurt to rn the activate command more than once) and install two packages we need.

``` bash
cd python_for_database_reporting
conda activate python_data_course
conda install jupyter psutil
```

To clone the repo:

``` bash  
git clone https://github.com/linuxacademy/content-python-for-database-and-reporting.git .
```


## Connecting to the Jupyter Notebook Server

### On the Playground Server

**Make sure that you have activated the virtual environment!**

To activate the virtual environment:

``` bash
conda activate python_data_course
```

To start the server run the following:

``` bash
python get_notebook_token.py
```

__This is a simple script that starts the jupyter notebook server and sets it to continue to run outside of the terminal.__

_```nohup jupyter notebook --no-browser --port=8086```_

_I have selected port 8086 but the actual port number is not important as long as you know what it is and it does not conflict with other running services._

_It then searches the resulting text file `nohup.out` to find and print the token._

**On the terminal is a token, please copy this and save it to a text file on your local machine.**

### On Your Local Machine

In a terminal window enter the following:

``` bash
ssh -N -L localhost:8087:localhost:8086 cloud_user@<the public IP address of the Playground server>
```

_-N indicates that there will be no remote commands_
_-L maps the local port to the remote port

_I have selected port 8087 for the local port but the actual port number is not important as long as you know what it is and it does not conflict with other running services._

It will ask you for your password, this is the password you use to login to the Playground remote server.

**Leave this terminal open, it will appear nothing has happened, but it must remain open while you use the Jupyter Notebook server in this session.**

In the browser of your choice enter the following address:

```http://localhost:8087```

This will open a Jupyter Notebook site that asks for the token you copied from the remote server.
