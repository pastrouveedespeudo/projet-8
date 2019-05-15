import psycopg2
from config import *
def choix_aliment_niveau_2():

    conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)                    
    cur = conn.cursor()
    


    cur.execute(""" create database postgres;
                """)

  
    conn.commit()


choix_aliment_niveau_2()
