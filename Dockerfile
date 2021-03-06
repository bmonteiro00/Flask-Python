#Use an official Python runtime as a parent image
FROM python:3.7-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#ENV MONGODB_HOST "localhost"
#ENV MONGODB_DATABASE "gitbase"

# Run app.py when the container launches
CMD ["python", "run.py"]

