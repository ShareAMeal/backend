#!/usr/bin/env sh
./manage.py migrate
./manage.py loaddata testdata.json
./manage.py runserver 0.0.0.0:8000