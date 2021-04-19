# Webservice PAEM
That webservice provide resources for using in PAEM UFOPA Project. This project aims to manage access of studanties and servers into the University 
by checking if the resources requested for that user is available and if the user is healthy. So, the project will have four application:
that webservice to manage data requested from other aplications; a system for manage the entrance for the concierge; a system for the user request entry into University
and finally a ChatBot for the user request entry as well.  

## Installations

### Prerequisites

#### Operational System Windows 7, 8 or 10

#### MySQL database.

We are current using [MySQL Comminity version 8.0.23](https://dev.mysql.com/downloads/installer/)

#### Python 3.7

You will need the Python 3.7. It's recomend download the latest version 3.7.x. To verify the installed version you have to follow the steps below:

1. Opend the command line (`CTRL+R` e digite _cmd_).

2. Type `python --version`.

If the version is presented correctly, Python is installed properly. The `python --version` command can't point to a version of Python 2.x.x.

If the Python are not installed or the version is incorrect, you need to make an alternative install of Python doing the following steps:

1. Download the python vesion [here](https://www.python.org/downloads/source/).

2. Remember to looking for 3.7.x version, where x is the latest version:

3. download the installer of 64 bits `Windows installer(64-bit)`.

4. Run the installer.

5. Check **install launch for all user** e **Add Python 3.8 to PATH** options.

6. Click __install Now__ option. Thus, Python will be installed correctly.

#### Pip
You will need Pip installed in the Python environment. If you followed the Python installation process described in this document, the Pip installation won't be necessary, so is **highly** recommended to follow the process described here even if you already have Python installed natively on Ubuntu.

To check if Pip is correctly installed, open the terminal and type one of the following commands:

```
> pip --version
> pip3 --version
> python -m pip --version
```

**Disclaimer**: If pip was not installed you need to install.

#### Pipenv

If you installed Python 3.8 according to this document, you can install Pipenv using:

```
> python -m pip install pipenv
or
> pip install pipenv
```

To check if the installation was successful use:

```
> python -m pipenv --version
or
> pipenv --version
```
Thus you can init the virtual enviroment into the repository typing `pipenv shell`. For [leanig other commands](https://github.com/pypa/pipenv).

#### Python libraries

To install the Python requirements open the command line in repository root and type the command `pip install -r \requirementes.txt`.

## Clone

To clone the repository follow the steps below:

1. Install the Git in your computer.
2. Click right mouse button.
3. Select `Git Bash here` option.
3. Clone repository typing `git clone https://github.com/flaviacomp/app-paem-db-restful.git`. Then now, start to code!

## Usage

#### Developer
The use of this repository is the same as the other Git repositories. Only a few differences need to be pointed out.

You **NEED** to use Pipenv for package management. Because of this it was installed and should be used from now on. 
You can learn how to use Pipenv [here](https://github.com/pypa/pipenv) and [here](https://pipenv.kennethreitz.org/en/latest/).

You should **NEVER** commit using the command `git commit -m <message>`. The `-m` parameter bypass the commit template. 
You should **ALWAYS** commit using just the command `git commit`.

#### Users
###### Getting starter
Considering usage in devoloping enviroment, you firt need to create a database run the script [create and import database](/create_import_db.py) 
by run `python create_import_db.py`. That create a database structure and import some data
test from csv files that there're into this repository. Then run the webserice by the command `python main_app.py` into this repository. 
Is the file [main app](/main.py). Thus, it's ready to make request to the server. By default the route server **http://localhost:5000** 

Some exemples of consuming this *webservice* is [here](/exemple) 

## Documentação

Webservice PAEM Documentation will be here in the future.
