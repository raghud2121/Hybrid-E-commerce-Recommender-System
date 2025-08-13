# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file first
COPY ./requirements.txt /code/requirements.txt

# --- COMBINED INSTALLATION LAYER ---
# Added backslashes (\) to continue the command across multiple lines
RUN apt-get update && \
    apt-get install -y build-essential && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt && \
    apt-get purge -y --auto-remove build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy the application source code and saved models into the container
COPY ./app /code/app
COPY ./saved_models /code/saved_models

# Command to run the application when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]