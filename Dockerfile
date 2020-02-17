FROM python:3.6-alpine
WORKDIR /server

COPY requirements.txt /server
RUN pip3 install -r requirements.txt
COPY . /server

CMD /server/manage.py runserver 0.0.0.0:8000
