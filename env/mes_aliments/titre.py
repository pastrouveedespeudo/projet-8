import psycopg2

def titre_aliment(para):

    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

                
    cur = conn.cursor()

    cur.execute("""SELECT name_aliment
                    FROM public.mes_aliments_aliment
                    WHERE name_aliment = '{}'""".format(para))
    conn.commit()
    
    rows = cur.fetchall()


    titre = [i for i in rows]
        
    print(titre,"123155555555555555555555555555555555555555")
    return titre

titre_aliment("Thé glacé Pêche")
