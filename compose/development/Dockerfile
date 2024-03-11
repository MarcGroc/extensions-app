FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/app
ENV PYTHONPATH /app/backend:$PYTHONPATH

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev \
    && rm -rf /var/cache/apk/*

COPY /backend/requirements/requirements.txt .
COPY /backend/requirements/dev-requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r dev-requirements.txt

COPY .. /app

RUN chmod +x /app/compose/development/start

CMD ["/bin/sh", "/app/compose/development/start"]
