# Time Series Forecasting and Benchmarks Repository

## Revision History

Zane Globus-O'Harra - 2023-05-04 - Add brief overview, authors,
technologies, requirements, installation instructions.

Zane Globus-O'Harra - 2023-05-05 - Add contact Zach W if installation or
runtime problems occur. Minor layout update.

## System Overview

The purpose of this application is to act as a central repository for time series (TS) data. 
Contributors will be able to upload their TS data along with a forecasting task for other users 
to complete. 

Data scientists or machine learning engineers can download the TS training data sets and 
create some predicted data. The data scientists can upload their solution data and see how it 
compares to the TS test data sets that the contributor uploaded.

For in-depth documentation, see `documentation/`

## Authors: 

CS 422 at the University of Oregon 

Team 1, "zeakz"

* Aiden Duval <aduval@uoregon.edu>
* Zane Globus-O'Harra <zfg@uoregon.edu>
* Erin Stone <estone3@uoregon.edu>
* Kareem Taha <kareemt@uoregon.edu>
* Zachary Weisenbloom <zweisenb@uoregon.edu>

## Technologies

* Django: High-level Python web framework
* SQLite Database: Built-in to Django
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

Navigate to the webpage,
[http://127.0.0.1:8000/home](http://127.0.0.1:8000/home).

If any issues occur while installing or running the application, please
contact Zachary Weisenbloom at <zweisenb@uoregon.edu>.

## Frontend Only Webapp

To run the app with all current functionality, follow the above
instructions. To see our intended design, with ***no backend
functionality***, navigate to 
[this website](https://pages.uoregon.edu/estone3/webapp/userchoose.html).