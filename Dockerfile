FROM python:3.13-slim

WORKDIR /task_site

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /task_site/static

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn task_site.wsgi:application --bind 0.0.0.0:8000"]