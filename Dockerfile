# # Use the official Python 3.11 image from the Docker Hub as the base image
# FROM python:3.11.2-slim

# # Set a working directory for the app inside the container
# WORKDIR /app

# # Copy the requirements file to the working directory in the container
# COPY requirements.txt .

# # Install the required Python libraries listed in requirements.txt
# RUN pip install -r requirements.txt

# RUN apt update -y && apt install awscli -y

# # Copy the current directory contents (your Flask app code) to /app in the container
# COPY . /app

# # Expose the port on which the Flask app will run
# #EXPOSE 5000

# # Set environment variables to avoid buffering issues with Flask
# #ENV PYTHONDONTWRITEBYTECODE 1
# #ENV PYTHONUNBUFFERED 1

# # Set the entry point for the container to run the Flask app
# CMD [ "python3","app.py"]

FROM python:3.11.2-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt
CMD ["python3", "app.py"]