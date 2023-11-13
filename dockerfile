FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

RUN pip install playwright
RUN apt-get update && apt-get -y install --no-install-recommends \
        ca-certificates \
        apt-transport-https \
        gnupg \
    && echo "deb http://deb.debian.org/debian buster main contrib non-free" > /etc/apt/sources.list \
    && echo "deb http://deb.debian.org/debian-security/ buster/updates main contrib non-free" >> /etc/apt/sources.list \
    && echo "deb http://deb.debian.org/debian buster-updates main contrib non-free" >> /etc/apt/sources.list \
    && apt-get update && apt-get install -y \
        libglib2.0-0 \
        libnss3 \
        libnspr4 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libcups2 \
        libdbus-1-3 \
        libdrm2 \
        libxcb1 \
        libxkbcommon0 \
        libatspi2.0-0 \
        libx11-6 \
        libxcomposite1 \
        libxdamage1 \
        libxext6 \
        libxfixes3 \
        libxrandr2 \
        libgbm1 \
        libpango-1.0-0 \
        libcairo2 \
        libasound2 \
    && rm -rf /var/lib/apt/lists/*

RUN playwright install

# Copy the content of the local src directory to the working directory
Add . .
