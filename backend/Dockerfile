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

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir debugpy


# Remove build tools after dependencies are installed.
RUN apt-get remove -y gcc g++ make libffi-dev musl-dev && apt-get autoremove -y


COPY . .

# Expose port 5678 for the debugger
EXPOSE 5678 5678

# start the server
CMD ["python", "-m", "debugpy", "--wait-for-client", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]