FROM python:3.6-jessie

MAINTAINER Matěj Račinský "racinsky.matej@seznam.cz"

WORKDIR /app

ADD ./*.py /app/
ADD ./config.yml /app/config.yml
ADD ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]