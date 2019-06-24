from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import JsonResponse

import random

import json as simplejson

from .verification_reponse import *
from .jeux import *


def niveau1(message):
    'this is function for lvl1'
    
    one = choice_food_level1()
    
    number = ["1","2","3","4"]

    image = [str(one[0][2]), str(one[1][0][2]), str(one[1][1][2]), str(one[1][2][2])]

    continuer = True
    while continuer:
    
        i = random.choice(image)
        j = random.choice(image)
        k = random.choice(image)
        l = random.choice(image)
        if i != j and i != k and i != l\
           and j != k and j != l\
           and k != l:
            continuer = False
            break
        else:
            j = l = k = ""

    data = {"image1":i, "image2":j,"image3":k,
            "image4":l,"yo":"coucou",
            'message':message}

    return data


def niveau2(message):
    'this is function for lvl2'

    one = choice_food_level2()

    picture = [one[0][0], one[1][0], one[1][1],
             one[1][2], one[1][3], one[1][4],
             one[1][5], one[1][6]]
    

    i = random.choice(picture)
    picture.remove(i)
    j = random.choice(picture)
    picture.remove(j)
    k = random.choice(picture)
    picture.remove(k)
    l = random.choice(picture)
    picture.remove(l)
    m = random.choice(picture)
    picture.remove(m)
    n = random.choice(picture)
    picture.remove(n)
    o = random.choice(picture)
    picture.remove(o)
    p = random.choice(picture)
  



    data = {"image1":i, "image2":j,"image3":k,"image4":l,
            "image5":m, "image6":n,"image7":o,"image8":p, 'message':message}

    return data



    
def niveau1_continuer(continuer):
    'this is function lvl1 continue'
    
    liste = [[], []]
    c = 0
    for i in continuer:
        for j in i:
            if j == ',':
                c+=1
            else:
                liste[c].append(j)

    liste2 = []
    for i in liste:
        liste2.append("".join(i))
    
    liste10 = []
    
    food = aliment.objects.filter(image=str(liste2[1])).all()
    for i in food:
        liste10.append(i.nutriscore)

    verif_nutri = liste10[0]
    

    if verif_nutri == "a":
        liste = ['<center><h1>bien joué</h1></center>',
                 '<center><h1>participe à top chef</h1></center>',
                 '<center><h1>formidable</h1></center>']
        message = random.choice(liste)
    else:
        liste = ['<center><h1>nul</h1></center>']
        
        message = random.choice(liste)

        
    niv1 = niveau1(message)
    return niv1


def niveau2_continuer(continuer):
    'this is function lvl2 continue'

    liste = [[],[],[],[],[],[]]
    c=0
    for i in continuer:
        if i == ',':
            c+=1
        else:
            liste[c].append(i)

    liste = ["".join(i) for i in liste]

    liste10 = []
    
    food_choose = aliment.objects.filter(image=liste[1]).all()
    
    for i in food_choose:
        liste10.append(i.nutriscore)
    nutriscore_id = liste10[0]


    if nutriscore_id == "a":
        message = "<h1><center>oui bonne réponse</h1></center>"
    else:
        message = "<h1><center>non mauvaise réponse</h1></center>"
    
    a = niveau2(message)
    return a



def jeux(request):

    current_user = request.user

    if request.method == "POST":

        niveau = request.POST.get('data')
        niveau = str(niveau)
  
        continuer = request.POST.get('data')
        continuer = str(continuer)

        current_user = request.user
 
        niveau_continuer = request.POST.get('data1')
     
        if niveau == "Niveau 1":
            lvl1 = niveau1('')
            return JsonResponse(lvl1)
        
        elif niveau == "Niveau 2":
            lvl2 = niveau2('')
            return JsonResponse(lvl2)

        elif niveau_continuer == "Niveau 2":
            lvl2_continue = niveau2_continuer(continuer)
            return JsonResponse(lvl2_continue)
        

        elif niveau_continuer == 'Niveau 1':
            lvl1_continue = niveau1_continuer(continuer)
            return JsonResponse(lvl1_continue)


    return render(request, "jeux.html")

