# Time Series Forecasting and Benchmarks Repository

TODO: app description 

# Authors: 

CS 422 at the University of Oregon 

Team 1, "zeakz"

* Aiden Duval <aduval@uoregon.edu>
* Zane Globus-O'Harra <zfg@uoregon.edu>
* Erin Stone <estone3@uoregon.edu>
* Kareem Taha <kareemt@uoregon.edu>
* Zachary Weisenbloom <zweisenb@uoregon.edu>

## Technologies

* Django: High-level Python web framework
* SQLite Database: Built in to Django
* HTML, CSS, JavaScript: For webpage display and UI design

## Requirements 

* Python 3
* pip
* virtualenv

## Installation

We assume that the user is using a Linux-based system. For installation steps that might be
different on other operating systems, links to additional instructions are provided.

* Django 4.2
* Pandas
* Grapher
* matplotlib

Install the requirements:

```
$ sudo apt install python3
$ python3 -m pip install --user --upgrade pip
$ python3 -m pip install --user virtualenv
```

Note: if you are using Windows, follow the instructions [here](https://www.python.org/downloads/) 
to install Python and [here](https://pip.pypa.io/en/stable/installation/) to install pip.

Clone the repository:

```
$ git clone https://github.com/zfgo/CS_422_p1.git
```

Navigate to the folder where the project was cloned:

```
$ cd CS_422_p1
```

Set up and run the virtual environment:

```
$ python3 -m venv env 
$ source env/bin/activate
$ python3 -m pip install -r requirements.txt
```

Note: if you are using Windows, follow the instructions 
[here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) 
for setting up a virtual environment.

Run the project:

```
$ python3 Django/mysite/zach_test/manage.py runserver
```

Navigate to the webpage, [http://127.0.0.1:8000/home](http://127.0.0.1:8000/home).
