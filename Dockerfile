FROM python:3.10-slim

WORKDIR /app

COPY /app .

RUN mkdir -p data

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
