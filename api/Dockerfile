FROM python:3.9.4-slim-buster

RUN apt-get update
RUN apt-get upgrade -y

COPY ./api /api
WORKDIR /api
RUN pip install -r requirements.txt

CMD ["python", "api.py"]