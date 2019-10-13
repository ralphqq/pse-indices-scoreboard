#!/bin/bash

set -euo

echo Starting up PostgreSQL

while !</dev/tcp/$DB_HOST/$DB_PORT; do
  sleep 0.1
done

echo PostgreSQL started

echo Activating virtual environment
source /home/venv/bin/activate

# Set secret key
export DJANGO_SETTINGS_MODULE=pse_summary.settings.production
echo SECRET_KEY=$(\
python -c"import random; print(''.join(random.SystemRandom().\
choices('abcdefghijklmnopqrstuvwxyz0123456789', k=50)))"\
) >> .env

echo Initializing db

python manage.py flush --no-input
python manage.py migrate

echo Starting up gunicorn

exec gunicorn -b :8000 --access-logfile - --error-logfile - pse_summary.wsgi:application