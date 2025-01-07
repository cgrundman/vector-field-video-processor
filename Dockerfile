# Use an official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY app/ /app/

# Install the required Python libraries
# RUN apt-get update && apt-get install -y python3-opencv
# RUN apt install libsm6
RUN pip install opencv-python==4.1.2.30

# Set the default command to run the application
CMD ["python", "app.py"]