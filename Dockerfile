FROM python:3.6-slim-buster
LABEL maintainer="ralph.quirequire@gmail.com"

# Install packages for psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev

# Create a nonroot user
RUN useradd -s /bin/bash psei

# Set working directory to this user's home directory
WORKDIR /home/psei

# Create a virtual environment
RUN python -m venv /home/venv

# Install dependencies and gunicorn app server
COPY requirements.txt .
RUN /home/venv/bin/pip install --upgrade pip
RUN /home/venv/bin/pip install -r requirements.txt
RUN /home/venv/bin/pip install gunicorn

# Copy project subdirectories to workdir
COPY index_scraper index_scraper
COPY main_board main_board
COPY pse_summary pse_summary

# Copy other top level files
COPY boot.sh manage.py secret-key.sh tickers.json ./

# Make entry point file executable
RUN chmod ugo+x boot.sh

# Set some environment variables
ENV DJANGO_SETTINGS_MODULE=pse_summary.settings.production
ENV CELERY_BROKER_URL=redis://redis:6379
ENV CELERY_RESULT_BACKEND=redis://redis:6379

# Set psei as workdir owner and current user (exclude venv dir)
RUN chown -R psei:psei ./
USER psei

# Ports and entrypoint are set in docker-compose.yml file