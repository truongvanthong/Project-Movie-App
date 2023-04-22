@echo off
python manage.py makemigrations

python manage.py migrate

@REM python manage.py createsuperuser