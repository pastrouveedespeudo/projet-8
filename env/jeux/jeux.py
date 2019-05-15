import sqlite3
import psycopg2
import random
from .config import *
from mes_aliments.models import *

def choix_aliment_niveau_1():

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


def choix_aliment_niveau_2():

    choice = aliment.objects.all().filter(nutriscore='a')
    food = random.choice(choice)
    picture = food.image

    liste_food_a = [picture]


    liste = []
    choice2 = aliment.objects.all().exclude(nutriscore='a')

    for i in choice2:
        liste.append(i.image)

    liste2 = []
    for i in range(7):
        random_food = random.choice(liste)
        liste2.append(random_food)
        
    return liste_food_a, liste2



































