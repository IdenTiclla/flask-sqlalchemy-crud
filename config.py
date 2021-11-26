from dotenv import load_dotenv
import os

load_dotenv()
user = os.environ['MYSQL_USER']
host = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DATABASE']

DATABASE_CONNECTION_URI = f'mysql://{user}@{host}/{database}'
