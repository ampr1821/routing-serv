FROM node:lts

RUN mkdir /app

WORKDIR /app

RUN apt update --quiet && apt install -y --quiet python3-venv libgdal-dev python3-dev

COPY requirements.txt /app

# setup virtual env and install dependencies
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
RUN mkdir venv/
RUN python3 -m venv venv/ && venv/bin/pip install wheel
RUN venv/bin/pip install -r requirements.txt

# node js setup
COPY package.json /app/

RUN npm install .

COPY . /app

ENTRYPOINT ["node", "index.js"]
