FROM python:latest

RUN apt-get update
RUN apt-get install -y curl

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --port 8000
