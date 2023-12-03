# Utilisez une image Debian de base
FROM debian

# Mise à jour des paquets et installation des dépendances
RUN apt-get update && apt-get install -y wget

# Téléchargez et installez le SDK .NET
RUN wget -O dotnet.tar.gz https://download.visualstudio.microsoft.com/download/pr/ce4b566e-5465-47e8-96ce-c702558c184f/20b9d9b647f3e65af91f7f8f01f30fc1/dotnet-sdk-5.0.400-linux-x64.tar.gz
RUN mkdir -p /usr/share/dotnet && tar -C /usr/share/dotnet -xzf dotnet.tar.gz
RUN ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet

# Copiez le code du worker dans le conteneur
COPY Program.cs /app/

# Définissez le répertoire de travail
WORKDIR /app

# Commande pour exécuter le worker
CMD ["dotnet", "run"]
