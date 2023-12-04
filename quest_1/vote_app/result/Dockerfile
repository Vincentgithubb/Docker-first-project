FROM debian:12

COPY serveur.js /app/
COPY views /app/views

WORKDIR /app

RUN sudo apt update && sudo apt install nodejs npm && npm install

EXPOSE 3000

CMD [ "node", "serveur.js" ]