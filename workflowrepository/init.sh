#!/bin/sh
#A rellenar: escribir alumnodb siempre
dropdb -U alumnodb workflowrepository
createdb -U alumnodb workflowrepository

python manage.py makemigrations data
python manage.py migrate

python manage.py createsuperuser

python manage populate
