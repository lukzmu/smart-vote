FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/
