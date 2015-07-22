FROM phusion/baseimage:0.9.12
MAINTAINER Justin Payne, justin.payne@fda.hhs.gov

RUN apt-get update && apt-get -y install \
	git \
    python3 \
    python3-dev \
    python3-pip \
    rabbitmq-server \
  && apt-get -y clean
  
RUN pip install flask celery

COPY . /code

RUN python /code/tests/__tests__.py
RUN export APP_NAME = "big-n-phylogeny-$(git describe)"