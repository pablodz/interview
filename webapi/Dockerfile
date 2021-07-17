# Download python docker
FROM python:3

# Create subdir to work
WORKDIR /usr/src/app

# Copy requirements of the webapi
COPY requirements.txt ./

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the files
COPY . .

# Check Python version
RUN python --version

# Run the main (DEBUG - WITHOUT WSGI)
CMD [ "python", "main.py" ]

# Run the main (PRODU - WITH WSGI) [BROKEN]
# ENTRYPOINT [ "bash","./gunicorn.sh" ]

# Open ports
EXPOSE 80