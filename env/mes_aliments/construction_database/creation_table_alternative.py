"""Here we creating tables for our database"""
import psycopg2

class create_tables:
    """creating tables"""

    def create_table_food(self):
        """Here we create food table"""

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD) 


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

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD) 
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

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD) 

        cur = conn.cursor()
        cur.execute("CREATE TABLE mes_aliments_categorie\
                    (id serial PRIMARY KEY,\
                    name_categorie VARCHAR(60) not null);")

        conn.commit()


    def create_table_search(self):
        """we create search table"""

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD) 
  
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




        
