FROM python:3.11.3

ARG app_dir=/app/

ADD requirements.txt $app_dir

WORKDIR $app_dir

RUN pip install --upgrade pip

RUN pip install -r requirements.txt