from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import psycopg2
from config import *

class delete:

    def delete_data_categorie(self):

        conn = psycopg2.connect(database="plateforme",
                                user="jb",
                                host="127.0.0.1",
                                password="tiotiotio333")
        

        cur = conn.cursor()
        
        cur.execute('''DELETE FROM mes_aliments_categorie''')
        conn.commit()

        print("categori supprimer gros, c la seul chose qui marche pour l'instant ")
    

    def delete_data_aliment(self):

        conn = psycopg2.connect(database="plateforme",
                                user="jb",
                                host="127.0.0.1",
                                password="tiotiotio333")

        cur = conn.cursor()
        
        cur.execute('''DELETE FROM mes_aliments_aliment''')
        conn.commit()

        print("aliment supprimer hihihi")

    def delete_tables_aliment(self):
        

        conn = psycopg2.connect(database="plateforme",
                                user="jb",
                                host="127.0.0.1",
                                password="tiotiotio333")

        cur = conn.cursor()
        
        cur.execute('''DROP TABLE mes_aliments_aliment''')
        conn.commit()

        print("database supprimer hihihi")

    def delete_tables_categorie(self):
        

        conn = psycopg2.connect(database="plateforme",
                                user="jb",
                                host="127.0.0.1",
                                password="tiotiotio333")
        cur = conn.cursor()
        
        cur.execute('''DROP TABLE mes_aliments_categorie''')
        conn.commit()

        print("database supprimer hihihi")


    def delete_tables_store(self):
        

        conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

        cur = conn.cursor()
        
        cur.execute('''DROP TABLE mes_aliments_store''')
        conn.commit()

        print("database supprimer hihihi")


    def delete_tables_brand(self):
        

        conn = psycopg2.connect(database="ddgh06joqvm83k",
                                user="giervvxxoatsci",
                                host="ec2-75-101-133-29.compute-1.amazonaws.com",
                                password="2d01f5ec86055f0422b819622bbb1e55a4dbd92d88d73ee9954c128b7aa8790c")

        cursor = conn.cursor()
        
        cursor.execute('''DROP TABLE mes_aliments_brand''')
        conn.commit()

        print("database supprimer hihihi")


yo = delete()
yo.delete_data_categorie()
yo.delete_data_aliment()
#yo.delete_tables_brand()
#yo.delete_tables_aliment()
#yo.delete_tables_store()
#yo.delete_tables_categorie()
