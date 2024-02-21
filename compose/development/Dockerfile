FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/app

WORKDIR /app
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev \
    && rm -rf /var/cache/apk/*

COPY /requirements/requirements.txt /app/
COPY /requirements/dev-requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir -r dev-requirements.txt

COPY . /app
RUN chmod +x /app/compose/development/start
CMD ["/bin/sh", "/app/compose/development/start"]
