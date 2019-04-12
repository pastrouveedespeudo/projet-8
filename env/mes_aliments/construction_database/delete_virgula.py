import psycopg2
from config import DATABASE, USER, HOST, PASSWORD



def del_vir():
    """Here we search food picture """
 
 
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 
    cur = conn.cursor()

    cur.execute("""UPDATE mes_aliments_aliment
                set name_aliment = REPLACE(name_aliment, ',', '');""")

    conn.commit()
    cur.execute("""select * from mes_aliments_aliment""")
    
    rows = cur.fetchall()
    print(rows)

del_vir()
