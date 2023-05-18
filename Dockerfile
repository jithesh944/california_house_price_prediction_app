FROM python:3.10
COPY . /docker_california_app
WORKDIR /docker_california_app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
