FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install django djangorestframework django-ckeditor django-redis googletrans==4.0.0-rc1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
