import os


db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']
db_database = os.environ['DB_DATABASE']
SQLALCHEMY_DATABASE_URL = f"mariadb+pymysql://{db_user}:{db_password}@{db_host}/{db_database}?charset=utf8mb4"
