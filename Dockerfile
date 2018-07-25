FROM python:3.6-jessie

MAINTAINER Matěj Račinský "racinsky.matej@seznam.cz"

WORKDIR /app

ADD ./* /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]