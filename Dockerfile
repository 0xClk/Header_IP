# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY app.py app.py

# Expose the port the app runs on
EXPOSE 7777

# Run the Flask app
CMD ["python", "app.py"]
