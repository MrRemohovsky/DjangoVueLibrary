FROM python:3.12-slim
WORKDIR /app/backend/locallibrary
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

