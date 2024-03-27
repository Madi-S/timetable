FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get -y install netcat-traditional gcc
RUN apt-get clean

RUN pip install --upgrade pip
COPY ./project/requirements.txt .
RUN pip install -r requirements.txt

COPY ./compose-web/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose-web/web_start /web_start
RUN sed -i 's/\r$//g' /web_start
RUN chmod +x /web_start

COPY ./compose-web/worker_start /worker_start
RUN sed -i 's/\r$//g' /worker_start
RUN chmod +x /worker_start

COPY ./compose-web/beat_start /beat_start
RUN sed -i 's/\r$//g' /beat_start
RUN chmod +x /beat_start

COPY ./compose-web/flower_start /flower_start
RUN sed -i 's/\r$//g' /flower_start
RUN chmod +x /flower_start

ENTRYPOINT ["/entrypoint"]