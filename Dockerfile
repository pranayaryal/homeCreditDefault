FROM jupyter/datascience-notebook

MAINTAINER Pranay Aryal

ADD . /home/jovyan

WORKDIR /home/jovyan

RUN pip install -r requirements.txt






