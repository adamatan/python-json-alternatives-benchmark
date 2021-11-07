FROM python:3.10-slim-bullseye

COPY requirements.txt /tmp
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
COPY src /src
COPY scripts /scripts
COPY pylintrc /pylintrc

CMD python3 src/benchmark.py
