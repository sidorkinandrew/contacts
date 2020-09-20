FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
# CMD uwsgi --module=myapp.wsgi --http=0.0.0.0:80