import sqlite3
import psycopg2
import random

import urllib.request
import shutil
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

import psycopg2
from PIL import Image

def new_table():
    
    conn = psycopg2.connect(database="deed0vc5eh1n6g",
                            user="hylgxgwfjacgtj",
                            host="ec2-54-225-95-183.compute-1.amazonaws.com",
                            password="2509ffb8ec855b2a37e2d1b80e0521d942219ad4d55a4abb6c1f5093000f6489")
    

    cur = conn.cursor()

    cur.execute("""create table niveau2(
                id serial PRIMARY KEY,
                image varchar(100));""")

    conn.commit()





    
def img_to_path():

    #path = r'C:\Users\jeanbaptiste\plateforme_nutella\platforme2\venv\plateforme\static\img_open'

    
    conn = psycopg2.connect(database="deed0vc5eh1n6g",
                            user="hylgxgwfjacgtj",
                            host="ec2-54-225-95-183.compute-1.amazonaws.com",
                            password="2509ffb8ec855b2a37e2d1b80e0521d942219ad4d55a4abb6c1f5093000f6489")


    cur = conn.cursor()

    cur.execute("""select * from mes_aliments_aliment where nutriscore != 'a';""")

    conn.commit()

    rows = cur.fetchall()

    liste = []
    for i in rows:
        c = 0
        for j in i:
            if c == 5:
                liste.append(j)
            c += 1

  
    c1 = 0
    for i in liste:
        nom = str(c1) + '.jpg'
        urllib.request.urlretrieve(i, nom)
       
        shutil.move(nom, r'C:\Users\jeanbaptiste\plateforme_nutella\platforme2\venv\plateforme\static\img_open')
        c1+=1

    return liste


def matching():

    os.chdir(r'C:\Users\jeanbaptiste\plateforme_nutella\platforme2\venv\plateforme\static\img_open')
    liste9 = os.listdir()
    print(len(liste9))
    c = 0

    for i in liste9:
        for j in liste9:
            if i == j:
                pass
            else:
                try:
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
                
                    if c < 300:
                        pass
                    else:
                        os.remove(j)

             
                    c = 0
                except:
                    pass
            
        c+=1
    
   




def insertion_database():
    

    os.chdir(r'C:\Users\jeanbaptiste\plateforme_nutella\platforme2\venv\plateforme\static\img_open')
    liste = os.listdir()

    print(len(liste))

    
    conn = psycopg2.connect(database="deed0vc5eh1n6g",
                            user="hylgxgwfjacgtj",
                            host="ec2-54-225-95-183.compute-1.amazonaws.com",
                            password="2509ffb8ec855b2a37e2d1b80e0521d942219ad4d55a4abb6c1f5093000f6489")


    cur = conn.cursor()

 
    cur.execute("""select * from mes_aliments_aliment where nutriscore != 'a';""")

    conn.commit()

    rows = cur.fetchall()

    liste1 = []
    for i in rows:
        c = 0
        for j in i:
            if c == 5:
                liste1.append(j)
            c += 1




            
    for i in liste:
        print(liste1[int(i[:-4])])



        cur.execute("""INSERT INTO niveau2(image)
                     VALUES((%s));""", (liste1[int(i[:-4])],))

        conn.commit()


def essais():
    conn = psycopg2.connect(database="deed0vc5eh1n6g",
                            user="hylgxgwfjacgtj",
                            host="ec2-54-225-95-183.compute-1.amazonaws.com",
                            password="2509ffb8ec855b2a37e2d1b80e0521d942219ad4d55a4abb6c1f5093000f6489")


    cur = conn.cursor()

 
    cur.execute("""select * from niveau2;""")

    conn.commit()

    rows = cur.fetchall()

    print(rows)

if __name__ == '__main__':

    #img_to_path()
    #matching()
    insertion_database()
    essais()

    #new_table()







