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

# Copy project directory to workdir
COPY . .

# Make boot.sh executable
RUN chmod ugo+x boot.sh 

# Set psei as workdir owner and current user (exclude venv dir)
RUN chown -R psei:psei ./
USER psei

# Specify port
EXPOSE 8000

# Set container entry point
ENTRYPOINT ["./boot.sh"]