import sqlite3
import psycopg2
import random
from .config import *
from mes_aliments.models import *
import urllib.request
import shutil
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def choice_food_level1():

    choice = aliment.objects.all().filter(nutriscore='a')
    food = random.choice(choice)
    name = food.name_aliment
    nutri = food.nutriscore
    picture = food.image

    liste_food_a = [name, nutri, picture]


    liste = []
    choice2 = aliment.objects.all().exclude(nutriscore='a')
    for i in choice2:
        liste.append((i.name_aliment, i.nutriscore, i.image))

    un = random.choice(liste)
    liste.remove(un)
    deux = random.choice(liste)
    liste.remove(deux)
    trois = random.choice(liste)

    
    liste_3_not_a = [un, deux, trois]


    return liste_food_a, liste_3_not_a


def choice_food_level2():

    
    choice = aliment.objects.all().filter(nutriscore='a')
    food = random.choice(choice)
    name = food.name_aliment
    nutri = food.nutriscore
    picture = str(food.image)

    liste_food_a = [picture]

    
    conn = psycopg2.connect(database="deed0vc5eh1n6g",
                            user="hylgxgwfjacgtj",
                            host="ec2-54-225-95-183.compute-1.amazonaws.com",
                            password="2509ffb8ec855b2a37e2d1b80e0521d942219ad4d55a4abb6c1f5093000f6489")


    cur = conn.cursor()

    cur.execute("""select * from mes_aliments_aliment where nutriscore != 'a';""")

    conn.commit()
    
    rows = cur.fetchall()

    the_liste = []
    for i in rows:
        c = 0
        for j in i:
            if c == 5:
                the_liste.append(j)
            c += 1

    #path = '/app/static/img_open'
    path = r'C:\Users\jeanbaptiste\plateforme_nutella\platforme2\venv\plateforme\static\img_open'
    os.chdir(path)
    liste = os.listdir()

    liliste = []
    for i in range(7):
 
        a = random.choice(liste)
        liliste.append(a)
        liste.remove(a)
  


    liste2 = []
    for i in liliste:
        liste2.append(the_liste[int(i[:-4])])

    
        
    return liste_food_a, liste2





























