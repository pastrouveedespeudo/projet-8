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
    picture = str(food.image)

    liste_food_a = [picture]


    liste = []
    c = 0
    choice2 = aliment.objects.all().exclude(nutriscore='a')
    
    for i in choice2:
        liste.append(str(i.image))
        nom = str(c) + '.jpg'
        urllib.request.urlretrieve(str(i.image), str(i.image))
        shutil.move(str(i.image), r'C:\Users\jeanbaptiste\plateforme_nutella\platforme2\venv\plateforme\static\img_open')
        c+=1
        
    liste = set(liste)
    liste = list(liste)


    os.chdir(r'C:\Users\jeanbaptiste\plateforme_nutella\platforme2\venv\plateforme\static\img_open')
    liste9 = os.listdir()

    c = 0
    
    for i in liste9:
        for j in liste9:
            
            img1 = cv2.imread(i)
            img2 = cv2.imread(j)

            orb = cv2.ORB_create()

            kp1, des1 = orb.detectAndCompute(img1,None)
            kp2, des2 = orb.detectAndCompute(img2,None)

            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1,des2)

            matches = sorted(matches, key = lambda x:x.distance)

            c = 0
            for match in matches:
                c+=1
        
            if c > 300:
                print(c)
            else:
                print(c)
                os.remove(j)

            c = 0

            
        c+=1

    liste10 = os.listdir()
    
    un = random.choice(liste10)
    liste.remove(un)
    deux = random.choice(liste10)
    liste.remove(deux)
    trois = random.choice(liste10)
    liste.remove(trois)
    quattre = random.choice(liste10)
    liste.remove(quattre)
    cinq = random.choice(liste10)
    liste.remove(cinq)
    six = random.choice(liste10)
    liste.remove(six)
    sept = random.choice(liste10)
    liste.remove(sept)

    
    liste2 = [un, deux, trois, quattre, cinq, six, sept]

    for i in liste2:
        print(i)
        print('\n')
        
    return liste_food_a, liste2



































