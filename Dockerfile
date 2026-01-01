FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .

ARG CACHE_BUSTER=1
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
CMD ["python", "main.py"]
