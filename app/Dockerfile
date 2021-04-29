FROM python:3.9.4-slim-buster

RUN apt-get update
RUN apt-get upgrade -y

COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]