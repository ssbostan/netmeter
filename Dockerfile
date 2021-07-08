FROM pypy:slim

LABEL maintainer="Saeid Bostandoust <ssbostan@linuxmail.org>"

EXPOSE 8080

ENV NETMETER_SYS_PATH=/sys

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8080 -w 2 \
  --access-logfile - --error-logfile - web:app
