FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./python/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./python/ /app/

CMD ["python", "main.py"]
