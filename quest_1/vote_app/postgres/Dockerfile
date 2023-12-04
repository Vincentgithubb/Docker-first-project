FROM debian:12

EXPOSE 5232

VOLUME [ "/var/lib/postgressql/data" ]

CMD ["postgressql", "--host", "0.0.0.0", "--port"? "5432"]