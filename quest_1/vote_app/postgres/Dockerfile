FROM debian:latest

EXPOSE 5232

VOLUME [ "/var/lib/postgressql/data" ]

CMD ["postgressql", "--bind", "0.0.0.0", "--port"? "5232"]