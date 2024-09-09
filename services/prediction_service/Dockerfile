# Use Python as base image
FROM python:3.12-alpine3.19

# Set the working directory
WORKDIR /app

# Install numpy, pandas, scikit-learn, and FastAPI
RUN pip install numpy pandas fastapi uvicorn
# scikit-learn dependencies
RUN apk add --no-cache gcc g++ make libffi-dev musl-dev python3-dev
RUN pip install scikit-learn

# Copy the requirements file and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Command to run when the container starts
CMD ["python", "main.py"]
