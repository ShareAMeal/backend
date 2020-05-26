#!/usr/bin/env sh
./manage.py migrate
./manage.py loaddata testdata.json
cd api && ../manage.py compilemessages
cd register && ../manage.py compilemessages
./manage.py runserver 0.0.0.0:8000