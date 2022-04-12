FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
    
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

# copy project
COPY ./src/ /app
WORKDIR /app

# copy docker-entrypoint.sh
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x ./docker-entrypoint.sh

# run docker-entrypoint.sh
# ENTRYPOINT ["bash", "docker-entrypoint.sh"]