# Download python docker
FROM python:3.8


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Open ports
EXPOSE 5000

WORKDIR /app

ADD . /app
