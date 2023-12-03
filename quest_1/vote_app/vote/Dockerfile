# Utilisez une image Python de base
FROM python:3.11-slim

# Copiez les fichiers nécessaires
COPY app.py requirements.txt /app/
COPY templates /app/templates
COPY static /app/static

# Définissez le répertoire de travail
WORKDIR /app

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Ouvrez le port par défaut de l'application
EXPOSE 5000

# Lancez le service de vote
CMD ["python", "app.py"]
