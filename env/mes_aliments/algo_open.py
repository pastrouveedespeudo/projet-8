import sqlite3
import psycopg2


def image_aliment(para):

    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

                    
    cur = conn.cursor()
    
    cur.execute("""select image, name_aliment
                from public.mes_aliments_aliment
                where name_aliment = '{}';
                """.format(para))
    conn.commit()
    
    rows = cur.fetchall()

    image = [i for i in rows]

    return image

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
        

    return titre


def better_nutri(para):

    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

                
    cur = conn.cursor()


    cur.execute("""SELECT id_categorie_id
    FROM public.mes_aliments_aliment
    WHERE name_aliment = '{}'""".format(para))

    conn.commit()

    rows = cur.fetchall()
    
    indice_cat = [i[0] for i in rows]


    cur.execute("""SELECT name_aliment, id_categorie_id, nutriscore, image,id
    FROM public.mes_aliments_aliment
    WHERE name_aliment = '{}'""".format(para))

    conn.commit()

    rows = cur.fetchall()

    aliment_recherché = [i for i in rows]

    
    c = 0
    for i in indice_cat:
        
        cur.execute("""SELECT name_aliment, id_categorie_id, nutriscore, image,id
        FROM public.mes_aliments_aliment
        WHERE id_categorie_id = {} and nutriscore != 'No_found' and image != 'No_found'
        ORDER BY nutriscore ASC""".format(indice_cat[c]))

        conn.commit()
        
        rows = cur.fetchall()

        liste = [i for i in rows]

            
        c+=1


    liste = liste[:6]
    liste[0] = aliment_recherché[0]
   
    return liste



def detail_aliment(value):

    detail = []
    
    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

                
    cur = conn.cursor()

    cur.execute("""SELECT *
                    FROM public.mes_aliments_aliment
                    WHERE id = {}""".format(value))


    conn.commit()

    rows = cur.fetchall()

    detail = [i for i in rows]
  
    return detail



def replace(para):

    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

                
    cur = conn.cursor()


    cur.execute("""SELECT id_categorie_id
    FROM public.mes_aliments_aliment
    WHERE name_aliment = '{}'""".format(para))

    conn.commit()

    rows = cur.fetchall()
    
    indice_cat = [i[0] for i in rows]


    c = 0
    for i in indice_cat:
        
        cur.execute("""SELECT name_aliment, id_categorie_id, nutriscore, image,id
        FROM public.mes_aliments_aliment
        WHERE id_categorie_id = {} and nutriscore != 'No_found' and image != 'No_found'
        and name_aliment != '{}'
        ORDER BY nutriscore ASC""".format(indice_cat[c], para))

        conn.commit()
        
        rows = cur.fetchall()

        liste = [i for i in rows]

            
        c+=1


    liste = liste[:6]
 
   
    return liste



def data_replace(request, username, aliment, new_aliment):
    
    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")                
    cur = conn.cursor()
    print(aliment)
    print(new_aliment)
    print("GOGODANCEUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUR")
    
    cur.execute("""UPDATE aliment_de_{}
                set name_aliment = '{}' where name_aliment = '{}'
              


                """.format(username,  new_aliment, aliment))

    
    conn.commit()

        
def verification_produit_pasèdeux_fois(username, produit):
##    
##    conn = psycopg2.connect(database="plateforme",
##                            user="postgres",
##                            host="127.0.0.1",
##                            password="tiotio")
    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")
                
    cur = conn.cursor()


    
    cur.execute("""SELECT * from aliment_de_{}
                WHERE name_aliment LIKE '%{}%'
              


                """.format(username, produit))

    
    conn.commit()


    rows = cur.fetchall()

    liste = [i for i in rows]

    if liste != []:
        return False
    else:
        return True






    
