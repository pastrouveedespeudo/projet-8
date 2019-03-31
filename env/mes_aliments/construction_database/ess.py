import psycopg2

conn = psycopg2.connect(database="plateforme",
                        user="postgres",
                        host="127.0.0.1",
                        password="tiotio")

            
cur = conn.cursor()

coucou = "coucou"
cur.execute("""insert into test (data) values('{0}')""".format(coucou))
conn.commit()
