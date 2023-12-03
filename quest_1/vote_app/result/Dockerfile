# Utilisez une image de Node.js de base
FROM debian

# Copiez les fichiers nécessaires
COPY server.js /app/
COPY views /app/views

# Définissez le répertoire de travail
WORKDIR /app

# Installez les dépendances
RUN npm install

# Ouvrez le port par défaut de l'application
EXPOSE 3000

# Lancez le service de résultats
CMD ["node", "server.js"]
