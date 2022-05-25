# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

EXPOSE 5000

CMD [ "gunicorn", "--workers", "1" ,"--bind", ":5000", "--proxy-protocol", "--reload", "--log-level", "debug","wsgi:app"]