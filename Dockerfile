FROM node:lts

RUN mkdir /app

WORKDIR /app

RUN apt update --quiet && apt install -y --quiet python3-venv

COPY requirements.txt /app

# setup virtual env and install dependencies
RUN mkdir venv/
RUN python3 -m venv venv/
RUN venv/bin/pip install -r requirements.txt

# node js setup
COPY package.json /app/

RUN npm install .

COPY . /app

ENTRYPOINT ["node", "index.js"]