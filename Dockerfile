# Use an official Python runtime as base image
FROM python:3.11-slim

# Set environment variables to prevent .pyc files and enable stdout logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy all project files to the container's working directory
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Download NLTK data required by your scripts
RUN python download_nltk_data.py

# Default command (you can change it as needed)
CMD ["python", "main.py"]
