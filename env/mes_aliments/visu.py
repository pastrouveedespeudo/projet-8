import psycopg2
def visualisation():
    """Here we search food picture """
 
 
    conn = psycopg2.connect(database='deed0vc5eh1n6g',
                            user='hylgxgwfjacgtj',
                            host='ec2-54-225-95-183.compute-1.amazonaws.com',
                            password='2509ffb8ec855b2a37e2d1b80e0521d942219ad4d55a4abb6c1f5093000f6489') 
    cur = conn.cursor()


    
    cur.execute("""select * from mes_aliments_aliment""")
    conn.commit()
    rows = cur.fetchall()
    print(rows)

visualisation()
