FROM postgres:latest

EXPOSE 5432

COPY initdb /docker-entrypoint-initdb.d/


VOLUME /var/lib/postgresql/data

CMD ["postgres"]
