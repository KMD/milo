# User Managment
## How to run?

Clone the repo:

`git clone <repo_url>`

*cd* to project folder:

`cd <project_folder>` 

Create virtual environment by:

`virtualenv --python=python3 venv`

Activate virtual environment:

`source venv/bin/activate`

Install requirements:

`pip install -r requirements.txt`

Make migrations:

`./manage.py makemigrations`

Migrate:

`./manage.py migrate`

Run server:

`./manage.py runserver`
