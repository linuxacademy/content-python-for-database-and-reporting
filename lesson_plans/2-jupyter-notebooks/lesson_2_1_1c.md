# Lesson Title

Installing Jupyter Notebooks, Opening a Notebook, and Setting the Kernel

## Description

A PDF is provided [here](https://linuxacademy-video.s3.amazonaws.com/guides/refsheets/setting_up_playground_server_1580153217.pdf?AWSAccessKeyId=ASIA3ETCCTRFDPW5E2WB&Expires=1580154117&Signature=ewGpzA0XkqfjUyE8vTPPLvq1iaw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBMaCXVzLWVhc3QtMSJHMEUCIHyMhrP2MFnHSzkOno1eQtmHbyZOyQftWnKZCmI%2FdXW1AiEA2Xge%2B1A8o%2BdXecAOq4%2BkVYyAK4x9vrki3S%2FOa8F2%2F%2B4q8wMIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw3NjU3ODM2MTI0OTAiDHIMgQcfWGhXOiqTvSrHAw4vNC9LkPAiFxJOJxSAKlfAX0RbjN5yEqOSEw7qNwT47Adz7rNrTskb%2BzeZRyLjdWzEtCZxFKKYGk1xJPVBQ0rKIkf2hWGheFJQ%2BsfNq3fp6BF%2FhY3a67SOYga7miwf38b51MQ4Kez3eqstCGIkcSQuXSgzO8c9v%2Bb1a8cs8cp9w8%2FwgMnn28JvMpHlXa%2FDydwkejdfUXBbIhyoVzNHvTSswPTnWfMOZgGBjT9eelodp4S4mETaNLKE7kB5gjg5O1vfj7LnIEk0HRcSxLcLL7u9ZgAckTuU5PkNspOQLmaIMb8NBj1aQ5nSzhA%2BFvTDRXGuGwxLeArDhhxgrIOM2FGtCQqbidAiEpIls%2Bm%2FbszxvfL5Mrx1WuluxgviE3%2FOxYaJCtEDgIupcuIINauS3cPpXBxL4p8YsvlMFWfsBD9lGY4XwjkaNQysP9DAdOmOdVtPumzQelMYqUcz26ydZmgvjBId6lvwQQAVaTyx8471%2FsbW4roYNnbcsY3IOniWuRYdD%2FGLG8%2FGH3BnBJzZjkcAmVFEmgg6TrRxH%2B9Hm7AeyuWkrPcAeh%2B6cHXSybtdolw8c634jhJ7yhY4frhd7lv3Y1WuaTY%2BML3bvPEFOu8BYuWtEg2XQBd3I6NYf%2FHon9lyrxmDlDcChIfE06O5fzqCvqbXGGrPCu7d6%2BK3iuzKdHCssrVqe2JQjQHxmu4S4TiTxwozsooqkOmx0q1jgT5vCaOZCfgGB8lbf3gLQrlMXLfc0Ibk6esVKZs%2F4s9ldG9qwidJpvuJjKENk%2Bil6XvsjPVLSADkutVTYRAJdse%2BQ%2FpU8m32F%2FMWC949VqmkQM%2BcwAkMQ6XyyZoJ2Mf%2FWpxdJ3L7%2FjoUvAr08GXyy0yCRvRvfC1derNCjjmWvj7O4LdzFF5vc0paow2RCVjC20DoLea7kC4WWwYNuIlBptI%3D).  This PDF documents the work we will be doing during this lesson.  It can be used in a variety of way but it is suggested that you download the PDF, watch through the entire lesson and then cmplete the steps on your own outside of the lesson.  Of course, you can use it to follow along with the lesson as you wish.

This is the same information as in the PDF:

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

## Tags

`Using Python for Data Management and Reporting` `python` `jupyter notebooks` `centos 7` `pyenv` `pipenv`

## Video
