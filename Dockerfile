
FROM ubuntu:16.04

# Install python3 and pip
RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y apt-transport-https curl \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql=13.0.1.0-1 mssql-tools=14.0.2.0-1 unixodbc-dev-utf16 locales \
    && ln -sfn /opt/mssql-tools/bin/sqlcmd-13.0.1.0 /usr/bin/sqlcmd \
    && ln -sfn /opt/mssql-tools/bin/bcp-13.0.1.0 /usr/bin/bcp \
    && locale-gen en_US.UTF-8 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8080

WORKDIR /usr/src/app/

RUN python3 manage.py collectstatic --no-input

CMD ["gunicorn", "updater.wsgi", "-b", "0.0.0.0:8080", "--timeout", "3600"]