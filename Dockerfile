FROM python:3.8.10-alpine

WORKDIR /app

RUN pip install flake8 flake8-docstrings pytest pytest-cov autopep8