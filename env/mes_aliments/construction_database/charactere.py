import psycopg2
from config import DATABASE, USER, HOST, PASSWORD



def replace():
    """Here we search food picture """
 
 
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 
    cur = conn.cursor()

    cur.execute("""UPDATE mes_aliments_aliment
                set name_aliment = REPLACE(name_aliment, '\xa0', '');""")

    conn.commit()
    


replace()
