"""Here we creating tables for our database"""
import psycopg2

class create_tables:
    """creating tables"""

    def create_table_food(self):
        """Here we create food table"""

        conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")


        cur = conn.cursor()

        cur.execute("""CREATE TABLE mes_aliments_aliment
                    (id serial PRIMARY KEY,
                    name_aliment TEXT not null,
                    code_product_food VARCHAR(40) not null,
                    description TEXT not null,
                    nutriscore VARCHAR(10) not null,
                    image TEXT not null,
                    name_store TEXT not null,
                    name_brand TEXT not null,
                    id_categorie_id INT not null);""")

        conn.commit()


    def create_table_substitute(self):
        """we creat food substitute"""

        conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE mes_aliments_substitut
                    (id serial PRIMARY KEY,
                    name_aliment TEXT not null,
                    code_product_food VARCHAR(40) not null,
                    description TEXT not null,
                    nutriscore VARCHAR(50) not null,
                    image TEXT not null,
                    name_store TEXT not null,
                    name_brand TEXT not null,
                    id_categorie_id INT not null);""")

        conn.commit()


    def create_table_category(self):
        """we create table category"""

        conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

        cur = conn.cursor()
        cur.execute("CREATE TABLE mes_aliments_categorie\
                    (id serial PRIMARY KEY,\
                    name_categorie VARCHAR(60) not null);")

        conn.commit()


    def create_table_search(self):
        """we create search table"""

        conn = psycopg2.connect(database="dcqhankmnah2r7",
                                user="nialuqvdnbwagj",
                                host="ec2-23-23-173-30.compute-1.amazonaws.com",
                                password="2462155ce31d6d2399f5e161e89355c8a499d2556781657526462dbf67b9ac18")
  
        cur = conn.cursor()
        cur.execute("CREATE TABLE mes_aliments_recherche\
                    (id serial PRIMARY KEY,\
                    recherche TEXT not null);")

        conn.commit()


if __name__ == "__main__":

    creation = create_tables()      
    creation.create_table_food()
    creation.create_table_substitute()
    creation.create_table_category()
    creation.create_table_search()




        
