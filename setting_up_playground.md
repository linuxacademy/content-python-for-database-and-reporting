# Creating Your Playground Server

 It is advised your start a Playground server to follow along with the lessons and practice on your own.

## Create a Playground server

We are going to create a simple Centos7 server and install what we need as we go along.  Choosing ```Centos 7``` will install a Centos 7 server with nothing extra added on.

Choose the following settings in making your Playground Server. You may choose a different tag if desired.

- Distribution: Centos7
- Zone: North America
- Size: Micro
- Tag: Using Python for Database Operations and Reporting

## SSH into your playground server

Once the server indicates it is ready, using your terminal:

``` text
ssh cloud_user@<listed public address>
```

- type `yes` when asked to allow connection to the server
- enter `<password listed>`
- You will be asked to change your password
- For Old Password, enter `<password listed>`
- For New Password, enter `your new password`
- Enter the New Password again, enter `your new password`
- Don't forget your new password!  You will use this new password when you log-in to your Playground server.

## Install Required Packages

We need to install git and several other packages that will allow us to create python virtual environments.

We will be using pyenv to allow us to easily install various python versions as we need.

``` text
sudo yum -y install epel-release git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel
```

## Install pyenv

Clone the repo.

``` text
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
```

After installing `pyenv` we need to update our bash profile to use it.

``` text
nano ~/.bashrc
```

Add the following to the end of your `.bashrc` file; this sets up pyenv to be used.

``` bash
## pyenv configs
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```

- type CTRL-X and enter `yes` to save the file

Restart your bash terminal to use the changes made using `source ~/.bashrc`

## Installing a Python3 Version

It is important to use a python3 version.  Centos 7 has not updated from python2.  So we will use pyenv to install a python3 version.  You may pick the python 3 version you want to use.  If you want to use the latest python3 it is version `3.8.1`. If you want to match the python3 version in our labs then use version `3.7.2`.  You can also use the same version as the version you use at work. However, caution is called for here, if the version used at your work is less than `3.6`, you will encounter errors in the Jupyter Notebooks. (We will be using `f-strings` introduced in `3.6`.)

Let's first look at what comes with Centos 7. Note the version numbers when you enter the following commands:

``` bash
python --version
```

``` bash
pip --version
```

Now we will install the version of python we want to use.  I will be matching the version used in the labs and that is `3.7.2`.  Please note: This may take a few minutes; it downloads the files and compiles it for this machinepyen.

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

To activate and use python 3.7.2:

``` bash
pyenv shell 3.7.2
```

This will take a few minutes becuase it is downlaoding files and then compiling them for use on the Centos 7 server.  Compilation is an expensive and time consuming process.

Now check to see that the pyenv shell is using the correct version of python and pip.

``` bash
pyenv exec python --version
```

``` bash
pyenv exec pip --version
```

Now we should make sure we are using the latest pip

``` bash
pyenv exec pip install --upgrade pip
```

Now you see we are using python 3.7.2 and the later version of pip.  We first need to install pipenv for you.

``` bash
pyenv exec pip install --user pipenv
```

## Use the git Repo for the Course

Now we will make a directory to hold our work and virtual envrionment.

``` bash
mkdir python_for_database_reporting
```

You change the above name to something you like if desired.

``` bash
cd python_for_database_reporting
```

Now we need to clone the git repo for the course

``` bash  
git clone https://github.com/linuxacademy/content-python-for-database-and-reporting.git .
```

Now we create the virtual environment for the course.

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

You only need to do this is you would like to practice using pyenv and pipenv and/or practice with your own data and Jupyter notebooks.

Create a directory for your work.

``` bash
mkdir <directory name>
```

``` bash
cd <directory name>
```

Now we need to create a virtual environment to hold the work/practice you will do. If you use a version other then `3.7.2` you will be informed that the version is not installed and ask if you want `pyenv` to install it.  You should type `yes`.

``` bash  
pipenv --python 3.7.2 # or whatver version you choose
```

To activate your new virtual environment:

``` bash
pipenv shell
```

To install packages needed for the work, you can add more later.

``` bash
pipenv install notebook numpy pandas
```
