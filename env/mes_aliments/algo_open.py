"""Here we discuss with database"""
import psycopg2

def image_aliment(para):
    """Here we search food picture """
 
 
    para = para.lower()
    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

                    
    cur = conn.cursor()
    
    cur.execute("""select image, LOWER(name_aliment)
                from public.mes_aliments_aliment
                where LOWER(name_aliment) LIKE '%{}%';
                """.format(para))
    
    conn.commit()
    
    rows = cur.fetchall()

    image = [i for i in rows]


    return image


def titre_aliment(para):
    """Here we search title picture """

    para = para.lower()
    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

                
    cur = conn.cursor()

    cur.execute("""SELECT LOWER(name_aliment)
                    FROM public.mes_aliments_aliment
                    WHERE LOWER(name_aliment) LIKE '%{}%'""".format(para))
    conn.commit()
    
    rows = cur.fetchall()


    titre = [i for i in rows]
        

    return titre




def better_nutri(para):


    para = para.lower()
   
    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

                
    cur = conn.cursor()



    cur.execute("""SELECT name_aliment from mes_aliments_aliment
                where LOWER(name_aliment) LIKE '%{}%'""".format(para))
    conn.commit()

    rows = cur.fetchall()


    cur.execute("""SELECT name_aliment, id_categorie_id, nutriscore, image,id
        FROM public.mes_aliments_aliment
        WHERE LOWER(name_aliment) = '{}'""".format(rows[0][0].lower()))

    conn.commit()

    rows = cur.fetchall()

    aliment_recherché = [i for i in rows]


    liste2 = []
    c = 0
    for i in range(20):

        cur.execute("""SELECT name_aliment, id_categorie_id, nutriscore, image
        FROM public.mes_aliments_aliment
        WHERE id_categorie_id = {} and nutriscore != 'No_found' and image != 'No_found'
        and LOWER(name_aliment) != '{}'
        ORDER BY nutriscore ASC""".format(aliment_recherché[0][1], para))

        conn.commit()
        
        rows = cur.fetchall()

        liste = [i for i in rows]
            

            
        c+=1


    liste = set(liste)
    liste = list(liste)
    liste = liste[:6]
    liste[0] = aliment_recherché[0]

    return liste


def food_details(value):
    """Here we calling informations about product. Thank to that we
    can redirect to Openfactfood"""

    details = []

    conn = psycopg2.connect(database="ddgh06joqvm83k",
                            user="giervvxxoatsci",
                            host="ec2-75-101-133-29.compute-1.amazonaws.com",
                            password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

    cur = conn.cursor()
    cur.execute("""SELECT *
                    FROM public.mes_aliments_aliment
                    WHERE image = '{}'""".format(value))

    conn.commit()
    rows = cur.fetchall()
    details = [i for i in rows]
    return details


def replace(para):
    """ """
    
    para = para.lower()
    
    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

                
    cur = conn.cursor()


    cur.execute("""SELECT id_categorie_id
    FROM public.mes_aliments_aliment
    WHERE LOWER(name_aliment) = '{}'""".format(para))

    conn.commit()

    rows = cur.fetchall()
    
    indice_cat = [i[0] for i in rows]
    indice_cat = indice_cat[0]


    c = 0
    for i in range(20):
        
        cur.execute("""SELECT distinct LOWER(name_aliment), id_categorie_id, nutriscore, image
        FROM public.mes_aliments_aliment
        WHERE id_categorie_id = {} and nutriscore != 'No_found' and image != 'No_found'
        and LOWER(name_aliment) != '{}'
        ORDER BY nutriscore ASC""".format(indice_cat, para))

        conn.commit()
        
        rows = cur.fetchall()

        liste = [i for i in rows]

            
        c+=1

    liste = set(liste)
    liste = list(liste)
    liste = liste[:6]
 
   
    return liste


def data_replace(request, username, aliment, new_aliment):
    """ """   


    
    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")                
    cur = conn.cursor()


    
    cur.execute("""UPDATE aliment_de_{}
                set name_aliment = '{}' where LOWER(name_aliment) = '{}'
              


                """.format(username,  new_aliment, aliment))

    
    conn.commit()

        
def verification_product_not_two(username, produit):
    """here we check that the food is not already present"""

    conn = psycopg2.connect(database="ddgh06joqvm83k",
                            user="giervvxxoatsci",
                            host="ec2-75-101-133-29.compute-1.amazonaws.com",
                            password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")
    cur = conn.cursor()

    cur.execute("""SELECT * from aliment_de_{}
                WHERE name_aliment LIKE LOWER('%{}%')
                """.format(username, produit))
    conn.commit()

    rows = cur.fetchall()
    liste = [i for i in rows]
    if liste == []:
        return True
    else:
        return False


def verification_remplacement(username, produit):
    """ """ 

    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")
                
    cur = conn.cursor()


    
    cur.execute("""SELECT name_aliment from aliment_de_{}
                WHERE name_aliment LIKE LOWER('%{}%')"""
                .format(username, produit))

    
    conn.commit()


    rows = cur.fetchall()

    liste = [i for i in rows]
   
    if liste == []:
        return True
    else:
        return False
