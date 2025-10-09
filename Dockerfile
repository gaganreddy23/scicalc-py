FROM python:3.11-slim

# Set working directory to project root inside container
WORKDIR /app

# Copy everything from current directory into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt pytest

# Default command: run your calculator.py
CMD ["python", "app/calculator.py"]
