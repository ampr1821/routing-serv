FROM python:latest

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN python3 -m venv venv/

RUN venv/bin/pip install -r requirements.txt

FROM node:latest

RUN mkdir /app

WORKDIR /app

COPY package.json /app/

RUN npm install .

COPY . /app

COPY --from=0 /app/venv /app

ENTRYPOINT ["node", "index.js"]