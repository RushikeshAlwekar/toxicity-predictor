# Use official Python image with version 3.10
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy everything into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port your app runs on
EXPOSE 10000

# Run the app
CMD ["python", "app.py"]
