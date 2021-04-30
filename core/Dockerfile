FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /backend
WORKDIR /backend
COPY . /backend/
RUN apt-get install python3-pip -y
RUN /venv/bin/pip install -U pip
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt
#RUN /venv/bin/python manage.py makemigrations --noinput
#RUN /venv/bin/python manage.py migrate
RUN if [ -f manage.py ]; then /venv/bin/python manage.py collectstatic --noinput; fi

EXPOSE 8000


