FROM ubuntu:18.10
WORKDIR /usr/src/app
RUN apt-get update -qq && \
    apt-get upgrade -qqy

RUN apt-get install -qqy \
    python-virtualenv \
    libpq-dev \
    python3-dev

RUN apt-get install python3-pip -y

COPY requirements.txt .
RUN virtualenv -q -p python3 venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

COPY run.py .
COPY . .
ENV FLASK_APP="run.py"
ENV FLASK_DEBUG=1
ENV POSTGRES_URL="0.0.0.0:5432"
ENV POSTGRES_USER="postgres"
ENV POSTGRES_PW="dbpw"
ENV POSTGRES_DB="test"
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY . .
CMD flask run --host=0.0.0.0
