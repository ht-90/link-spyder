# Base image
FROM python:3.7-slim

# Username
USER root

# Update linux and vim
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y vim less

# Install pip and setuptools
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# Copy requirements file and move to workspace
WORKDIR /home/link-spyder
COPY requirements.txt ${PWD}

# Install python packages
RUN pip install -r requirements.txt
