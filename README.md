# Django CRM

A simple customer relationship manager built with Django. Users sign up and log in, then manage customer records.

## Features

- Sign up, log in and log out with Django's authentication
- List all customer records on the home page once you're logged in
- Add, view, update and delete a record: name, email, phone, address, city, state and ZIP code
- Pages are only available to logged-in users
- Flash messages for each action
- Bootstrap layout with a navbar

## Pages

| Path | What it does |
| --- | --- |
| `/` | Log in, or see all records |
| `/register/` | Sign up |
| `/logout/` | Log out |
| `/add_record` | Add a record |
| `/record/<id>` | View a record |
| `/update_record/<id>` | Edit a record |
| `/delete_record/<id>` | Delete a record |

## Built with

- Python 3, Django
- MySQL
- Bootstrap

## Run it locally

You need a MySQL server running locally.

```bash
git clone https://github.com/hamzakhalem/CRM.git
cd CRM
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django mysqlclient
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
```

Create a database named `ourcode` and set your MySQL user and password in `DATABASES` in `crmproject/settings.py`. Then:

```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000, sign up, and start adding records.

## Project structure

```
crmproject/   Project settings and root URLs
website/      Record model, sign-up form, record form, views and templates
```
