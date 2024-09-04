# Use Python as base image
FROM python:3.12-alpine3.19

# Install numpy, pandas, and scikit-learn
RUN pip install numpy pandas
# scikit-learn dependencies
RUN apk add --no-cache gcc g++ make libffi-dev musl-dev python3-dev
RUN pip install scikit-learn

# Set the working directory
WORKDIR /app

# Command to run when the container starts
CMD ["/bin/sh"]