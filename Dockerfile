# Use the official Python image from the Docker Hub
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# configure certs
COPY certs.pem .
ENV REQUESTS_CA_BUNDLE=/code/certs.pem
ENV SSL_CERT_FILE=/code/certs.pem

# Copy requirements.txt
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "livereload", "0.0.0.0:8000"]