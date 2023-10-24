from python:3.10.8-slim

run apt update

run pip install pipenv

copy src /app

workdir /app

run pipenv install

run apt install -y libmariadb-dev wget curl build-essential 
run wget https://r.mariadb.com/downloads/mariadb_repo_setup \
    && mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
run apt update