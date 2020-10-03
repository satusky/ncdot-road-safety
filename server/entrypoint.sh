#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

export DJANGO_SUPERUSER_PASSWORD="admin123"
python manage.py collectstatic --no-input --clear
#python manage.py makemigrations rs_core --noinput
python manage.py migrate sites --noinput
python manage.py migrate --no-input
python manage.py createsuperuser --username admin --email admin@example.com --no-input

exec "$@"
