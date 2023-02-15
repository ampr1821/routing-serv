FROM node:latest

RUN mkdir /app

WORKDIR /app

COPY package.json /app/

RUN npm install .

ENTRYPOINT["node", "index.js"]