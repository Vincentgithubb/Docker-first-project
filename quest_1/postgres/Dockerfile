# Image Debian
FROM debian

# PostgreSQL
RUN apt update && apt install -y postgresql postgresql-contrib

# Port
EXPOSE 5432

# Volume
VOLUME ["/var/lib/postgresql/data"]

# Run PostgreSQL
CMD ["postgres"]
