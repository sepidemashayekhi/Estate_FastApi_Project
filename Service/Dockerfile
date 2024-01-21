
FROM python:3.9-slim-buster

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

ENV SQL_SERVER_HOST=local
ENV SQL_SERVER_PORT=1433
ENV SQL_SERVER_DATABASE=mydatabase
ENV SQL_SERVER_USER=myuser
ENV SQL_SERVER_PASSWORD=mypassword

CMD uvicorn main:app --host 0.0.0.0 --port 8000
