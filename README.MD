#CIDM6325 - Fall 2022
##Django for Beginers
### Chapter 1 Steps
1. Create virtual environment on windows: `python -m venv .venv`
2. Activate virtual enviroment on windows: `source .venv/Scripts/activate`
3. Create a project: `django-admin startproject ProjectName .`
4. Run the project: `./manage.py runserver`

Django Secret Key Generator: https://django-secret-key-generator.netlify.app/

### Chapter 4

Variations to the steps:
1. cd onedrive\desktop\code
1. mkdir message-board
1. cd message-board
1. python -m venv .venv
1.  .venv\Scripts\Activate.ps1
1. (.venv) > python -m pip install django~=4.0.0
1. (.venv) > django-admin startproject django_project .
1. (.venv) > python manage.py startapp posts