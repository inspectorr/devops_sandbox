FROM python:3.12.8-bookworm

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN addgroup --system appgroup && \
    adduser --system --group appgroup && \
    chown -R appgroup:appgroup /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

USER appgroup

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

