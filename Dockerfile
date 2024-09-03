# Use Python as base image
FROM python:3.12-alpine3.19



# Install numpy, pandas, and scikit-learn
RUN pip install numpy pandas
# troubles installing scikit-learn with pip, but with packages it's okay
RUN apk add py3-scikit-learn

# Copy the news.csv file into the container
COPY news.csv /app/news.csv

# Copy the script file into the container
COPY detect_fake.py /app/detect_fake.py

# Set the working directory
WORKDIR /app

# Command to run when the container starts
CMD ["/bin/sh"]
