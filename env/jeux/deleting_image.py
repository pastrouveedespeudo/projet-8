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

def delete():

    path = r'C:\Users\jeanbaptiste\plateforme_nutella\platforme2\venv\plateforme\static\img_open'

    
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

    print(liste)
    c1 = 0
    for i in liste:
        nom = str(c1) + '.jpg'
        urllib.request.urlretrieve(i, nom)
       
        shutil.move(nom, path)
        c1+=1


    path = r'C:\Users\jeanbaptiste\plateforme_nutella\platforme2\venv\plateforme\static\img_open'
    path1 = r'C:\Users\jeanbaptiste\plateforme_nutella\platforme2\venv\plateforme\static\img_open\{}'
    os.chdir(path)
        

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
    
    liliste = os.listdir()
    print(len(liliste))


delete()
