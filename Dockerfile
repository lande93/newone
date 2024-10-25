# Use the official Python 3.11 image from the Docker Hub as the base image
FROM python:3.11.2-slim

# Set a working directory for the app inside the container
WORKDIR /app

# Copy the requirements file to the working directory in the container
COPY requirements.txt .

# Install the required Python libraries listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents (your Flask app code) to /app in the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set environment variables to avoid buffering issues with Flask
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the entry point for the container to run the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "application:app"]
