"""This is functions for searching from database"""

import psycopg2

def controle_data_food(username):
    """Here we watch if user have 6 products,
    if he has -6 we ask him to select products
    else we warned him to modify his selection"""

    conn = psycopg2.connect(database="ddgh06joqvm83k",
                            user="giervvxxoatsci",
                            host="ec2-75-101-133-29.compute-1.amazonaws.com",
                            password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

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

    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")       
    cur = conn.cursor()
    cur.execute("""INSERT INTO aliment_de_{}
                    (name_aliment, username)
                    VALUES (LOWER('{}'), '{}');""".format(username, food_name, username))
    conn.commit()
