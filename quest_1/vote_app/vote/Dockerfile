FROM python:3.11-slim

COPY app.py requirements.txt /app/
COPY templates /app/templates
COPY static /app/static
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
