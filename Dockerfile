FROM python:3.7
WORKDIR /code

COPY ./requirements.txt requirements.txt
RUN pip install requirements.txt
EXPOSE 5000
COPY . .
CMD ['python manage.py runserver']
