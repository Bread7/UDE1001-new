# Resource Web using Django
0 security. **ZERO**.<br />
This is a rough prototype that was developed.\
Duplicate and use at your own cost. Not liable for any issues faced.
## Purpose
Our goal is to help lower income students to gather free resources and opportunities to help develop their character and passion. 

## Usage Guide (MacOS tested)
Ensure that postgresql has been setup

Install all necessary modules
`pip install -r requirements.txt`

Migrate models into database
`python manage.py migrate`

Seed data
`python manage.py loaddata *.json`

Runserver
`python manage.py runserver`
## Tools needed
Python >3.10.6\
Django >4.1\
Postgres >14


## Notes
Generate list of installed modules\
`conda env export > environment.yml`\
`pip list --format=freeze > requirements.txt`

To seed data: use dumpdata -> loaddata\
Before dumping data, manually edit the table with data to get sample json output\
`python manage.py dumpdata --indent 4 > users.json`