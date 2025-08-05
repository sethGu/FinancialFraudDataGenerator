FROM python:3.10

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/backend

COPY . /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="/app:/app/smart_finance_main:$PYTHONPATH"

EXPOSE 9528

CMD ["python", "manage.py", "runserver", "0.0.0.0:9528"]