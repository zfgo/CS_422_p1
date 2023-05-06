# Developer Documentation

### Revision History

Zane Globus-O'Harra - 2023-05-04 - Start developer documentation.

Zane Globus-O'Harra - 2023-05-05 - Finish developer documentation

## Setup

Please follow the [installation
instructions](https://github.com/zfgo/CS_422_p1/blob/main/README.md).

## High-level overview

The home page will be used to provide users with the choice of
registering as a contributor or as a participant. If they choose to be a
contributor, they can upload TS data sets and forecasting tasks. The
forecasting task information and TS data sets are stored in a database
by the system, where the train data sets can be retrieved for
participants to download and the test data sets can be compared to the
participants uploaded solution data to produce metrics.

## Directory overview

The code for the main app is stored in `Django/mysite/`. This directory
also contains the database, and the manage script, which is used to
start the system. The `Django/mysite/documents/` directory is where the
TS data files are saved. The `Django/mysite/downloads/` directory is
where files are saved before they are downloaded. The
`Django/mysite/mysite/` directory contains the app settings as well as
URL patterns that the app uses. The `Django/mysite/static/` directory
contains the static elements for the application's UI design. The
`Django/mysite/zach_test/` directory contains the functionality of the
main system. Inside this directory, there are the following files and
directories: 

* `views.py`: Code for the views, which call the forms and request the
  templates to display the dynamic elements of the web app.
* `urls.py`: Contains the URL patterns that the app uses.
* `forms.py`: Code that helps get inputted information from the users
  and save it to a model.
* `models.py`: Contains the task and document models, which are saved in
  the database.
* `templates/`: HTML for the web app.

For more in-depth information about the decisions made during the design
of the system, please read the SDS, software design specification.

Additionally, each file and function should be sufficiently documented
for new developers to understand what the code does, which should allow
them to edit or change the system themselves.