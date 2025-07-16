FROM python:3.12-slim


WORKDIR /app


COPY requirements.txt .

COPY docker/entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh


RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    gettext \
    vim \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/nexus_crm


CMD ["sh", "-c", "python manage.py migrate && gunicorn nexus_crm.wsgi:application --bind 0.0.0.0:8000"]