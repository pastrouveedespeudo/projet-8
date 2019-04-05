"""Here we discuss with database for
food from user database"""

import psycopg2

def mes_aliment_user(username):
    """Here we take user food"""

    conn = psycopg2.connect(database="ddgh06joqvm83k",
                            user="giervvxxoatsci",
                            host="ec2-75-101-133-29.compute-1.amazonaws.com",
                            password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

    cur = conn.cursor()

    try:
        cur.execute("""SELECT * FROM aliment_de_{0}
                    """.format(username))
        conn.commit()
        rows = cur.fetchall()
        food_user = [i for i in rows]
        food = [i[1] for i in food_user[1:]]
        return food

    except:
        pass


def display_food(liste_aliment):
    """Here we take informations food for template"""
 
    conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")
    cur = conn.cursor()
    liste_ali = []
    try:
        for i in liste_aliment:
            cur.execute("""SELECT distinct name_aliment,
                        code_product_food,description,nutriscore,
                        image,name_store,name_brand
                        FROM public.mes_aliments_aliment
                        where LOWER(name_aliment) = '{}'
                        """.format(i))
            conn.commit()

            rows = cur.fetchall()
            for i in rows:
                liste_ali.append(i)
        c=0

        return liste_ali

    except:
        pass
