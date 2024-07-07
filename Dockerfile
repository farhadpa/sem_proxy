FROM python:3.11-alpine3.17

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY ./requirements.txt /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080


# Run proxy.py when the container launches
CMD ["python", "proxy.py"]


