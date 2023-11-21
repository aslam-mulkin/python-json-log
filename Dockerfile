FROM python:3.8-slim

WORKDIR /app

COPY log_generator.py /app/log_generator.py

CMD ["python", "./log_generator.py"]
