FROM debian

RUN apt-get update && apt-get install -y wget

RUN wget -O dotnet.tar.gz https://download.visualstudio.microsoft.com/download/pr/ce4b566e-5465-47e8-96ce-c702558c184f/20b9d9b647f3e65af91f7f8f01f30fc1/dotnet-sdk-5.0.400-linux-x64.tar.gz
RUN mkdir -p /usr/share/dotnet && tar -C /usr/share/dotnet -xzf dotnet.tar.gz
RUN ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet

COPY Program.cs /app/

WORKDIR /app

CMD ["dotnet", "run"]
