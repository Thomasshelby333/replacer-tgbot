# Use the official Python base image with the desired Python version
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt

# Install the Python dependencies
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
