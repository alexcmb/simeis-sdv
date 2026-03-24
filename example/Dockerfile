FROM python:3.11-alpine

WORKDIR /app

# Copy the client script into the container
COPY client.py .

# Run the client script, allowing arguments to be passed (e.g., docker run my-client <username>)
ENTRYPOINT ["python", "client.py"]
