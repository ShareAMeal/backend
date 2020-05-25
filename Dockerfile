FROM python:3.6
WORKDIR /server

COPY requirements.txt /server
RUN pip3 install -r requirements.txt
COPY . /server

CMD /bin/sh /server/startme.sh
