FROM python:3.9-slim

# Install Node.js for Playwright
RUN apt-get update && apt-get install -y nodejs npm

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install

# Copy the content of the local src directory to the working directory
COPY . .

# Command to run on container start
CMD ["python", "./script.py"]