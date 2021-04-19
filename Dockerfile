FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN /venv/bin/python manage.py makemigrations --noinput
RUN /venv/bin/python manage.py migrate
RUN /venv/bin/python manage.py runserver
COPY . /code/

