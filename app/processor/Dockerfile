FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ../shared /app/shared
COPY . /app

CMD ["python", "processor/main.py"]
