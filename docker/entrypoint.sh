#!/bin/bash

set -e


echo "Cборка статики..."
python manage.py collectstatic --noinput


echo "Запуск сервера..."
exec "$@"