FROM debian:12

COPY Program.cs /app/


WORKDIR /app


RUN sudo apt update && sudo apt install -y wget


RUN wget https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN sudo dpkg -i packages-microsoft-prod.deb
RUN rm packages-microsoft-prod.deb

RUN sudo apt-get update && \
    sudo apt-get install -y dotnet-sdk-8.0

RUN sudo apt-get update && \
   sudo apt-get install -y aspnetcore-runtime-8.0


CMD ["dotnet", "run"]
