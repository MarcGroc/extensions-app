FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app/backend:$PYTHONPATH

WORKDIR /app

# Installing dependencies
RUN apk update && \
    apk add --no-cache gcc musl-dev postgresql-dev && \
    rm -rf /var/cache/apk/*

# Copying requirements files and installing Python dependencies
COPY backend/requirements/requirements.txt .
COPY backend/requirements/dev-requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r dev-requirements.txt

COPY ./backend/ .

RUN chmod +x /app/scripts/start
RUN sed -i 's/\r$//' /app/scripts/start
CMD ["/bin/sh", "/app/scripts/start"]
