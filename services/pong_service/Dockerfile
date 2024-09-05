# Use Python as base image
FROM python:3.12-alpine3.20

# Set the working directory
WORKDIR /app

COPY ./app /app

# Install FastAPI
RUN pip install --no-cache-dir -r requirements.txt

# You need to mount the shared_models to the docker
# docker run -v /path/to/shared_models:/app/shared_models ...

EXPOSE 8000

# Command to run when the container starts
CMD ["python", "main.py"]