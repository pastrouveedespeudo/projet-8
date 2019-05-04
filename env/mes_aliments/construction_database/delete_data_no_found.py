import psycopg2
from config import DATABASE, USER, HOST, PASSWORD



def dela():
    """Here we search food picture """
 
 
    conn = psycopg2.connect(database='plateforme',
                            user='jb',
                            host='127.0.0.1',
                            password='tiotiotio333') 
    cur = conn.cursor()

    cur.execute("""DELETE FROM mes_aliments_aliment
                WHERE nutriscore = 'no_found' or
                image = 'no_found' or name_aliment='no_found'
                or code_product_food = 'no_found'""")

    conn.commit()
    cur.execute("""select * from mes_aliments_aliment""")
    
    rows = cur.fetchall()
    print(rows)

dela()
