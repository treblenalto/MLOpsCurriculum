FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

# copy project
COPY ./src/ /app
WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]