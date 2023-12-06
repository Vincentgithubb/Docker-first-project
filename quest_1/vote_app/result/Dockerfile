FROM debian

COPY server.js /app/
COPY views /app/views

WORKDIR /app

RUN npm install

EXPOSE 3000

CMD ["node", "server.js"]
