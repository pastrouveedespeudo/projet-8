"""Here we create database user"""

import psycopg2
from .config import DATABASE, USER, HOST, PASSWORD

def create_database_user(username):
    """Here we create database user"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)      

    cur = conn.cursor()

    cur.execute("""CREATE TABLE aliment_de_{}
                (id serial PRIMARY KEY,
                name_aliment TEXT,
                username VARCHAR(20) not null
                );""".format(username))

    conn.commit()


def insert_database_user(username):
    """Here we insert name user into his database"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)                     
    cur = conn.cursor()


    cur.execute("""INSERT INTO aliment_de_{0}
                (username)
                VALUES('{1}');""".format(username, username))

    conn.commit()
