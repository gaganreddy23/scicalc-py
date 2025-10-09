FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

COPY app /app/app
COPY requirements.txt /app/
COPY test_calculator.py /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt pytest


# Default command: run calculator.py
CMD ["python", "calculator.py"]
