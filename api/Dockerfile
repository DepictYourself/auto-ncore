FROM --platform=linux/arm/v7 arm32v7/python:3.11-slim-bullseye


# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libffi-dev \
    musl-dev \
    && apt-get clean

    
# set the working directory
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# Remove build tools after dependencies are installed.
RUN apt-get remove -y gcc g++ make libffi-dev musl-dev && apt-get autoremove -y


COPY . /app

# start the server
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]