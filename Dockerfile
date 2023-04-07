FROM python:3.9.16-slim

# Create working directory
RUN mkdir /app
WORKDIR /app

COPY *.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt
RUN python3 download_graph.py

ENTRYPOINT ["python3", "-u", "flask_server.py"]