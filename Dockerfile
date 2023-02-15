FROM python:latest

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN python -m venv venv/ && source venv/bin/activate

RUN pip install -r requirements.txt

FROM node:latest

COPY package.json /app/

RUN npm install .

COPY . /app

ENTRYPOINT ["node", "index.js"]