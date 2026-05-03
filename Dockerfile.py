FROM debian:stable-slim

WORKDIR /app

RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*

COPY main.py main.py
COPY books/ books/
CMD ["python3", "main.py"]