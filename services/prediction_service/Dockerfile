# Use Python as base image
FROM python:3.12-alpine3.19

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# scikit-learn dependencies
RUN apk add --no-cache gcc g++ make libffi-dev musl-dev python3-dev && \
    pip install --no-cache-dir -r requirements.txt

# Command to run when the container starts
CMD ["python", "main.py"]
