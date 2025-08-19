FROM python:3.12.0

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["gunicorn", "dan_dasakami.wsgi:application", "--bind", "0.0.0.0:8000"]