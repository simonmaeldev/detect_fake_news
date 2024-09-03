# Use Ubuntu as the base image
FROM ubuntu:latest

# Update and install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install numpy, pandas, and scikit-learn
RUN pip3 install numpy pandas scikit-learn

# Copy the news.csv file into the container
COPY news.csv /app/news.csv

# Set the working directory
WORKDIR /app

# Command to run when the container starts
CMD ["/bin/bash"]
