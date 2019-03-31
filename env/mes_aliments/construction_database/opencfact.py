"""Here we insert data into our database from api openfactfood"""

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json
import psycopg2


class data:

    
    def categorie(self):

        conn = psycopg2.connect(database="dcqhankmnah2r7",
                                user="nialuqvdnbwagj",
                                host="ec2-23-23-173-30.compute-1.amazonaws.com",
                                password="2462155ce31d6d2399f5e161e89355c8a499d2556781657526462dbf67b9ac18")


##        conn = psycopg2.connect(database="plateforme",
##                                user="postgres",
##                                host="127.0.0.1",
##                                password="tiotio")

        cursor = conn.cursor()
        
        self.liste = []

        path = "https://fr.openfoodfacts.org/categories"
        
        requete = requests.get(path)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")

        for tag in soup.find_all("td"):
            self.liste.append(tag.text)

        c = 0
        for i in range(3):
            print(self.liste[c])
            
            self.liste[c] = self.liste[c].replace(" ", "_")
            self.liste[c]= self.liste[c].replace("'", "")
            
            cursor.execute("INSERT INTO mes_aliments_categorie(name_categorie) VALUES ('{0}')".format(str(self.liste[c])))
            conn.commit()
            c+=3


    def insert_food(self):
        """Here we run api and we take informations necessary for tables insertion"""


        conn = psycopg2.connect(database="dcqhankmnah2r7",
                                user="nialuqvdnbwagj",
                                host="ec2-23-23-173-30.compute-1.amazonaws.com",
                                password="2462155ce31d6d2399f5e161e89355c8a499d2556781657526462dbf67b9ac18")


##        conn = psycopg2.connect(database="plateforme",
##                                user="postgres",
##                                host="127.0.0.1",
##                                password="tiotio")

        cursor = conn.cursor()
 

        
        c = 0
        d = 1
        self.liste_store = []
        self.liste_store1 = [[], [], [], [], [], [], [], [],
                             [], [], [], [], [], [], [], [],
                             [], [], [], [], [], [], [], []]
        
        self.liste_brands = []
        self.liste_brands1 = [[], [], [], [], [], [], [], [],
                              [], [], [], [], [], [], [], [],
                              [], [], [], [], [], [], [], []]
        
        
        self.liste2 = []
        
        for i in range(3):

            print(self.liste[c])
            print("\n")
            
            path2 = "https://fr.openfoodfacts.org/categorie/{}".format(self.liste[c])
            requete = requests.get(path2)
            page = requete.content
            soup = BeautifulSoup(page, "html.parser")
            for tag in soup.find_all("span"):
                self.liste2.append(tag.text)

            for i in self.liste2[6:]:
                print(i)
                a = str(i).find(" - ")
                i = i[0:a]
                print(i)
                path3 = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms={}&json=1"
                search = path3.format(i)
                r = requests.get(search)
                data = json.loads(r.text)
                
                try:
                    self.number_product = data["products"][0]['code']
                except:
                    self.number_product = "No_found"
                try:
                    self.description_product = data["products"][0]["ingredients_text_fr"]
                except:
                    self.description_product = "No_found"
               
                try:
                    self.nutriscore = data["products"][0]["nutrition_grades"]
                    print("nutriscore=",self.nutriscore)
                except:
                    self.nutriscore = "No_found"

                try:
                    self.image = data["products"][0]["image_front_url"]
                except:
                    self.image = "No_found"


                try:
                    self.brandss = data["products"][0]["brands"]
                    if self.brandss == '':
                        self.liste_brands.append(self.brandss)
                    else:
                        self.liste_brands.append(self.brandss)
                except:
                    self.brandss = "No_found"
                    self.liste_brands.append("No_found")



                try:
                    self.store_product = data["products"][0]["stores"]
                    if self.store_product == '':
                        self.liste_store.append("No_found")
                    else:
                        self.liste_store.append(self.store_product)
                except:
                    self.store_product = "No_found"
                    self.liste_store.append("No_found")

                i = i.replace("'", "")
                print(i)
                self.image = self.image.replace("'", "")
                print(self.number_product)
                
                self.description_product = self.description_product.replace("'", "")
            
                print(self.description_product)
                self.nutriscore = self.nutriscore.replace("'", "")
            
                print(self.nutriscore)
                self.nutriscore = self.nutriscore.replace("'", "")
           
                print(self.image)
                self.image = self.image.replace("'", "")
            
                print(d)
               
                print(self.store_product)
                self.store_product = self.store_product.replace("'", "")
            
                print(self.brandss)
                self.brandss = self.brandss.replace("'", "")

                
                
                
                cursor.execute("INSERT INTO mes_aliments_aliment (name_aliment,\
                                image, code_product_food, description, nutriscore,\
                                id_categorie_id, name_store, name_brand)\
                                VALUES('{0}','{1}','{2}','{3}','{4}',{5},'{6}','{7}')"\
                               .format(i, self.image, self.number_product, self.description_product,
                                       self.nutriscore,
                                       d, self.store_product,self.brandss ))


       
                conn.commit()


                
 
            d+=1
            c+=3
            self.liste2 = []


                                                












yo = data()           
yo.categorie()
yo.insert_food()

