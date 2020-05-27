#!/usr/bin/env sh
./manage.py migrate
./manage.py loaddata testdata.json
pwd
ls
cd api && ../manage.py compilemessages && cd ..
cd register && ../manage.py compilemessages && cd ..
./manage.py runserver 0.0.0.0:8000
