FROM debian:12

RUN apt-get update && apt-get install -y postgresql

COPY ./postgres/postgres.env /etc/postgres.env
VOLUME /var/lib/postgresql/data

EXPOSE 5432

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=db
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=4000

CMD ["/usr/lib/postgresql/15/bin/postgres", "-h", "0.0.0.0"]