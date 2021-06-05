# Projeto do Bootcamp Fullstack

 - Python
 - Django
 - Postgres

Step by Step

## Instalação do django 
"""
conda install django
"""

conda create --name cserver python=3

Para criar um novo projeto com nome project_name
django-admin startproject {project_name}

Criação do ambiente virtual
python3 -m venv ac

cria uma nova aplicacao web em python
python manage.py startapp {project_name}

python manage.py runserver

Create models
python manage.py makemigrations
Do migration
python manage.py migrate

python manage.py createsuperuser
