# Image Debian
FROM debian

# Redis
RUN apt update && apt install -y redis-server

# Port
EXPOSE 6379

# Run Redis
CMD ["redis-server"]
