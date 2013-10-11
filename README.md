Website of the Dublin University Computer Science Society. This site is built with Mezzanine, which is 
a Python Django blog system.


Development
===============

## Installation

### First Off
Make sure you have install `python-dev` and `python-pip` before continuing
To install them run:
```bash
sudo apt-get install python-dev
sudo apt-get install python-pip
```

### Virtualenv and Dependencies
Suggested that you run the project inside a virtualenv. It isolates your global python package library from your development package library. This reduces the risk of conflicts and reduces risk of you accidentally breaking python packages across your system.

To globally install virtualenv run
```bash
pip install virtualenv
```
Go to the root directory of this repository and run this command to create a virtualenv
```bash
./create_virtual_env.sh
```
To activate the virtualenv run
```bash
source env/bin/activate
```
From now on any packages you install will be specific to this virtualenv. You must activate the env every time you want to install packages or run the code in this project.

### Setup
You will have to setup a fake database at the start for you to dev with. The fastest way to do that is:
```bash
cd project
python manage.py sync
```

## Running the Development Server
Running the following command will setup a simple python webserver and run Mezzanine. 
```bash
python manage.py runserver 8080
```
To site is located at http://localhost:8080

Deployment
==========

Web server running python. Should really run on a solid database like MySQL in production and not on SQLite like in development. Having memcached installed and working in production is also a big plus.


Design info
===========
The black is #2d2d2d, the orange is #ff8b0f, the background is #eaeaea with a white radial gradient underneath the logo and the font is PT Sans

