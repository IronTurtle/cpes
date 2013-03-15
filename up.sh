#!/bin/sh

python manage.py sqlclear challenge
python manage.py sqlall challenge
python manage.py syncdb
