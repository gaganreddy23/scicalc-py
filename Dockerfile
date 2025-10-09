FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy calculator.py into container
COPY app/ /app

# Copy requirements.txt and tests from root
COPY requirements.txt /app/
COPY test_calculator.py /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt pytest

# Default command: run calculator.py
CMD ["python", "calculator.py"]
