FROM debian:12

EXPOSE 6379

RUN apt-get update && apt-get install -y redis-server

CMD ["redis-server", "--bind", "0.0.0.0", "--port", "6379"]
