# Lesson Title

Installing Jupyter Notebooks, Opening a Notebook, and Setting the Kernel

## Description

A PDF is provided [here](https://linuxacademy-video.s3.amazonaws.com/guides/refsheets/setting_up_playground_server_1580153217.pdf?AWSAccessKeyId=ASIA3ETCCTRFDPW5E2WB&Expires=1580154117&Signature=ewGpzA0XkqfjUyE8vTPPLvq1iaw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBMaCXVzLWVhc3QtMSJHMEUCIHyMhrP2MFnHSzkOno1eQtmHbyZOyQftWnKZCmI%2FdXW1AiEA2Xge%2B1A8o%2BdXecAOq4%2BkVYyAK4x9vrki3S%2FOa8F2%2F%2B4q8wMIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw3NjU3ODM2MTI0OTAiDHIMgQcfWGhXOiqTvSrHAw4vNC9LkPAiFxJOJxSAKlfAX0RbjN5yEqOSEw7qNwT47Adz7rNrTskb%2BzeZRyLjdWzEtCZxFKKYGk1xJPVBQ0rKIkf2hWGheFJQ%2BsfNq3fp6BF%2FhY3a67SOYga7miwf38b51MQ4Kez3eqstCGIkcSQuXSgzO8c9v%2Bb1a8cs8cp9w8%2FwgMnn28JvMpHlXa%2FDydwkejdfUXBbIhyoVzNHvTSswPTnWfMOZgGBjT9eelodp4S4mETaNLKE7kB5gjg5O1vfj7LnIEk0HRcSxLcLL7u9ZgAckTuU5PkNspOQLmaIMb8NBj1aQ5nSzhA%2BFvTDRXGuGwxLeArDhhxgrIOM2FGtCQqbidAiEpIls%2Bm%2FbszxvfL5Mrx1WuluxgviE3%2FOxYaJCtEDgIupcuIINauS3cPpXBxL4p8YsvlMFWfsBD9lGY4XwjkaNQysP9DAdOmOdVtPumzQelMYqUcz26ydZmgvjBId6lvwQQAVaTyx8471%2FsbW4roYNnbcsY3IOniWuRYdD%2FGLG8%2FGH3BnBJzZjkcAmVFEmgg6TrRxH%2B9Hm7AeyuWkrPcAeh%2B6cHXSybtdolw8c634jhJ7yhY4frhd7lv3Y1WuaTY%2BML3bvPEFOu8BYuWtEg2XQBd3I6NYf%2FHon9lyrxmDlDcChIfE06O5fzqCvqbXGGrPCu7d6%2BK3iuzKdHCssrVqe2JQjQHxmu4S4TiTxwozsooqkOmx0q1jgT5vCaOZCfgGB8lbf3gLQrlMXLfc0Ibk6esVKZs%2F4s9ldG9qwidJpvuJjKENk%2Bil6XvsjPVLSADkutVTYRAJdse%2BQ%2FpU8m32F%2FMWC949VqmkQM%2BcwAkMQ6XyyZoJ2Mf%2FWpxdJ3L7%2FjoUvAr08GXyy0yCRvRvfC1derNCjjmWvj7O4LdzFF5vc0paow2RCVjC20DoLea7kC4WWwYNuIlBptI%3D).  This PDF documents the work we will be doing during this lesson.  It can be used in a variety of ways but it is suggested that you download the PDF, watch through the entire lesson and then cmplete the steps on your own outside of the lesson.  Of course, you can use it to follow along with the lesson as you wish.

This is the same information as in the PDF:

# Creating Your Playground Server

 It is advised your start a Playground server to follow along with the lessons and practice on your own.

## Create a Playground server

We are going to create a simple Centos7 server and install what we need as we go along.  Choosing **`Centos 7`** will install a basic Centos 7 server.

### Playground Server Settings

Choose the following settings in making your Playground Server. You may choose a different tag if desired.

- Distribution: Centos7
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

## Install Required Packages

We need to install git and several other packages that will allow us to create python virtual environments.

We will be using pyenv to allow us to easily install various python versions as we need.

``` bash
sudo yum -y install epel-release git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel

```

### Install pyenv

Clone the repo.

``` bash
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
```

After installing **`pyenv`** we need to update the **`.bashrc`** file to use it.

``` bash
nano ~/.bashrc
```

Copy and paste the following to the end of your **`.bashrc`** file

``` bash
## pyenv configs
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```

When you have copied the above to the .bashrc file, press CTRL-X and then select **`y`**.

Restart your bash terminal to use the changes made using

``` bash
source ~/.bashrc
```

## Installing a Python 3 Version

It is important to use a Python 3 version for our work; Python 2 is no longer supported.  Centos 7 has not updated from Python 2.  As a result we will use pyenv to install a Python 3 version.  

You may pick the Python 3 version you want to use.  If you want to use the latest Python 3 it is version **`3.8.1`** at the time of this writing. If you want to match the Python 3 version in our labs, then use version **`3.7.2`**; this is the version we will be using in the labs and for our lessons.  You can also use the same version as you use at work. However, caution is called for, if the version used at work is less than **`3.6`**, you will encounter errors in the Jupyter Notebooks. (We will be using **`f-strings`** introduced in **`3.6`**. As a result, an earlier version will result in errors.)

Let's  determine the Python version that comes with Centos 7. Note the version numbers when you enter the following commands:

``` bash
python --version
```


``` bash
pip --version
```

Now lets install the Python version we want, namely `3.7.2`.
 **Please note: This may take a few minutes; it downloads the files and compiles it for this machine. Compiling a program can take some time.**

``` bash
pyenv install 3.7.2
```

Let's first look at the version numbers again. Note the version numbers have not changed, pyenv installed python 3.7.2 but it is not activated for use.

``` bash
python --version
```

``` bash
pip --version
```

To set pyenv to use Python 3.7.2:

``` bash
pyenv shell 3.7.2
```

To use the pyenv Python version we use **`exec`**, this stands for execute:

``` bash
pyenv exec python --version
```

``` bash
pyenv exec pip --version
```

Now you see we are using python 3.7.2 and the later version of pip.  

Let's update pip to the latest version:

``` bash
pyenv exec pip install --upgrade pip
```

Now we need to install pipenv.

``` bash
pyenv exec pip install --user pipenv
```

## Use the git Repo for the Course to Practice What We Do in Lessons

Now we will make a directory to hold our work and virtual envrionment.

``` bash
mkdir python_for_database_reporting
```

**You change the above name to something you like if desired.**

``` bash
cd python_for_database_reporting
```

Now we need to clone the git repo for the course

``` bash  
git clone https://github.com/linuxacademy/content-python-for-database-and-reporting.git .
```

To create the virtual environment and install the packages we will use:
**Please note: you can use **`ls`** to verify there is a **`Pipfile`** in the directory.

``` bash
pipenv install
```

To activate your new virtual environment:

``` bash
pipenv shell
```

This activates the new environment.  Now all python work will use the packages and versions installed into this virtual environment.

Let's first look at the version numbers again. Note the version numbers are for python 3.7.2.

``` bash
python --version
```

``` bash
pip --version
```

If you need to add a python package not already installed:

``` bash
pipenv install <package-name>
```

To leave the virtual environment:

``` bash
exit
```

## (OPTIONAL) Create an Environment for Your Practice

**You only need to do this is you would like to practice using pyenv and pipenv and/or practice with your own data and Jupyter notebooks.

Create a directory for your work.

``` bash
mkdir <directory name>
```

``` bash
cd <directory name>
```

Now we need to create a virtual environment to hold the work/practice you will do. If you use a version other then **`3.7.2`** you will be informed that the version is not installed and ask if you want **`pyenv`** to install it.  You should type **`yes`**.

``` bash  
pipenv --python 3.7.2 # or whatver version you choose
```

To activate your new virtual environment:

``` bash
pipenv shell
```

Now install the basic required packages:

``` bash
pipenv install notebook numpy pandas
```

To install packages later:

``` bash
pipenv install <packages name(s)>
```

## Tags

`Using Python for Data Management and Reporting` `python` `jupyter notebooks` `centos 7` `pyenv` `pipenv`

## Video
