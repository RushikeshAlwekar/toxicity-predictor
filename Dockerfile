# Use Python 3.10 base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (for numpy, scikit-learn, nltk etc.)
RUN apt-get update && apt-get install -y gcc

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port (if needed for Render, usually 10000 or 5000)
EXPOSE 10000

# Start your app
CMD ["python", "app.py"]
