FROM --platform=linux/arm/v7 arm32v7/python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD [ "python", "main.py" ]