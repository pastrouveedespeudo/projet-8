"""This is functions for searching from database"""

import psycopg2
from .config import DATABASE, USER, HOST, PASSWORD

def controle_data_food(username):
    """Here we watch if user have 6 products,
    if he has -6 we ask him to select products
    else we warned him to modify his selection"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    cur.execute("""SELECT COUNT(name_aliment) FROM aliment_de_{0}
                    """.format(username))
    conn.commit()
    rows = cur.fetchall()
    count_food = [i for i in rows]

    if count_food[0][0] >= 6:
        return "nombre de produit suppérieur a 6", False
    
    else:
        return "stockage du produit possible", True


def insert_food(username, food_name):
    """He we insert food"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)       
    cur = conn.cursor()
    cur.execute("""INSERT INTO aliment_de_{}
                    (name_aliment, username)
                    VALUES (LOWER('{}'), '{}');""".format(username, food_name, username))
    conn.commit()
