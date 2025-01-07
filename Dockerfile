# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app/ /app/

# Install dependencies
RUN pip install -r ./app/requirements.txt

# Set the default command to run the app.py script
CMD ["python", "app.py"]