# Utilisez l'image de base
FROM Debian

# Ouvrez le port par défaut de Redis
EXPOSE 6379

# Lancez le container dans le réseau back-end
CMD ["redis-server", "--bind", "0.0.0.0", "--port", "6379"]
