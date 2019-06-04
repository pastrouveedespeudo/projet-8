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

    cur.execute("""select image from niveau2;""")

    conn.commit()
    
    rows = cur.fetchall()

    liste = []
    for i in rows:
        liste.append(i[0])


    liste2 = []
    for i in range(7):
        a = random.choice(liste)
        liste2.append(a)
        liste.remove(a)



    return liste_food_a, liste2





























