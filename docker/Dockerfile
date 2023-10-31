from python:3.10.8-slim

run apt update \
    && apt install -y wget curl build-essential

run wget https://r.mariadb.com/downloads/mariadb_repo_setup \
    && bash mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
run apt update \
    && apt install -y libmariadb-dev

run pip install pipenv

copy src /app

workdir /app

run pipenv install
