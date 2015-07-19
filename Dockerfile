FROM phusion/baseimage:0.9.12
MAINTAINER Justin Payne, justin.payne@fda.hhs.gov

RUN apt-get update && apt-get -y install \
    python3 \
  && apt-get -y clean