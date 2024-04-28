FROM node:20.12

WORKDIR /app

COPY ./frontend .

RUN chmod +x /app/scripts/start

CMD ["/bin/sh", "/app/scripts/start"]
