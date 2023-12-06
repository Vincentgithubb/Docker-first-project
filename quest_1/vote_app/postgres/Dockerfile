FROM debian:12

EXPOSE 5232

RUN apt-get update && \
    apt-get install -y postgresql

COPY ./initdb /docker-entrypoint-initdb.d/

VOLUME [ "/var/lib/postgresql/data" ]

CMD ["postgresql"]