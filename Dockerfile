FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

# copy project
COPY ./src/ /app
WORKDIR /app

# copy docker-entrypoint.sh
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

# run docker-entrypoint.sh
ENTRYPOINT ["bash", "docker-entrypoint.sh"]