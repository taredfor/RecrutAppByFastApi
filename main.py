from fastapi import FastAPI
from data_request_model import User
import psycopg2
from sqlalchemy import create_engine

app = FastAPI()

HOST_DB = 'localhost'
PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'qwerty123'
MYSQL_DB = 'Recrut'
@app.get('/')
async def test():
    return {'hello': 'recrut'}


@app.post('/add-user')
async def add_user(parameters: User):
    conn = psycopg2.connect(host=HOST_DB, port=PORT, database=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASSWORD)
    cur = conn.cursor()
    cur.execute("INSERT INTO users(first_name, second_name, planet, e_mail) VALUES(%s,%s,%s,%s)", parameters.first_name, parameters.second_name, parameters.planet, parameters.e_mail)
    conn.commit()
    conn.close()
    cur.close()
    return 'User is added'