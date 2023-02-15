FROM python:latest

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN python -m venv venv/ && venv/bin/activate

RUN pip install -r requirements.txt

FROM node:latest

RUN mkdir /app

WORKDIR /app

COPY package.json /app/

RUN npm install .

COPY . /app

COPY --from=0 /app/venv /app

ENTRYPOINT ["node", "index.js"]