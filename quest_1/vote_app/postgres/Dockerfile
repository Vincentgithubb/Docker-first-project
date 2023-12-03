# Utilisez l'image de base
FROM postgres:latest

# Exposez le port par défaut de PostgreSQL
EXPOSE 5432

# Copiez le script d'initialisation dans le conteneur
COPY initdb /docker-entrypoint-initdb.d/


# Mettez en place un volume pour les données persistantes
VOLUME /var/lib/postgresql/data

# Lancez le container dans le réseau back-end
CMD ["postgres"]
