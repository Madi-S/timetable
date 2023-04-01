FROM python:3.10.1-slim-buster

# Set workdir
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr 
ENV PYTHONUNBUFFERED 1

# Update apt-get and install/upgrade system dependencies 
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# Upgrade pip and install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Coppy application files
COPY . .

# Copy entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]