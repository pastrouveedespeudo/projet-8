"""This is views for food stuff"""

from django.shortcuts import render
from django.db import models
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import JsonResponse
from .mes_aliments_preferer_user import *
from django.shortcuts import redirect
from .algo_open import *
from .mes_aliments_user import *

def food_det(request):
    """This is function for food details"""

    if request.method == "POST":
        
        search = request.POST.get('produit')
        details = food_details(search)
        url_nutri = details.nutriscore
        food = details.name_aliment
        code = details.code_product_food
        image = details.image
        url_nutri = "/static/img/portfolio/nutriscore/" + str(url_nutri) + ".jpg >"

        return render(request, 'aliment_det.html',{'detail':details,
                                                   'url_nutri':url_nutri,
                                                   'code':code,
                                                   'image':image,
                                                   'aliment': food
                                                   })
    return render(request, 'aliment_det.html')



@csrf_exempt
def searching(request):
    """Here we can searching into database"""

    liste_recherche = []
    exceeded_stock = ""
    current_user = request.user
    
    if request.method == "POST":

        search = request.POST.get('cool')
        username = request.POST.get('username')
        validate = request.POST.getlist('data[]')
        try:
            stock = controle_data_food(current_user)
        except:
            pass
        if validate and username:

            current_user = request.user
            stock = controle_data_food(username)
            
            if stock[1] == True:
                veri = verification_product_not_two(current_user,
                                                    validate[0])
       
                if veri == True:
                   
                    insert_food(username, validate[0])
                    print("aliment pas deja")
                    
            elif stock[1] == False:
                print('aliment deja')
                exceeded_stock = "oups vous avez trop d'aliment en stock supprime en ! ou remplace le !"

        if search:
      
            current_user = request.user

            if current_user.is_authenticated:

                stock = controle_data_food(current_user)

                if stock[1] == False:
                    exceeded_stock = "oups vous avez trop d'aliment en stock supprime en ! ou remplace le !"
        
            image = image_aliment(search)
            title = titre_aliment(search)

            try:
 
                a = better_nutri(search)
     
                return render(request, 'recherche.html',
                              {"a":str(a[0][3]),
                               "b":str(a[1][3]),
                               "c":str(a[2][3]),
                               "d":str(a[3][3]),
                               "e":str(a[4][3]),
                               "f":str(a[5][3]),

                               "aa":str(a[0][0]),
                               "bb":str(a[1][0]),
                               "cc":str(a[2][0]),
                               "dd":str(a[3][0]),
                               "ee":str(a[4][0]),
                               "ff":str(a[5][0]),

                               "aaa":str(a[0][3]),
                               "bbb":str(a[1][3]),
                               "ccc":str(a[2][3]),
                               "ddd":str(a[3][3]),
                               "eee":str(a[4][3]),
                               "fff":str(a[5][3]),

                               "aaaa":"/static/img/portfolio/nutriscore/" + str(a[0][2]) + ".jpg >",
                               "bbbb":"/static/img/portfolio/nutriscore/" + str(a[1][2]) + ".jpg >",
                               "cccc":"/static/img/portfolio/nutriscore/" + str(a[2][2]) + ".jpg >",
                               "dddd":"/static/img/portfolio/nutriscore/" + str(a[3][2]) + ".jpg >",
                               "eeee":"/static/img/portfolio/nutriscore/" + str(a[4][2]) + ".jpg >",
                               "ffff":"/static/img/portfolio/nutriscore/" + str(a[5][2]) + ".jpg >",

                               "image":str(image),
                               "titre":str(title),
                               "stock_depassé":exceeded_stock,
                               })

            except:
                message = "oups nous n'avons pas cet aliment en database"
                return render(request, 'error.html', {"message":message})

    image = '/static/img/header1.jpg'
    return render(request, 'recherche.html', {'image':image})



def my_food(request):
    """Here we acced to user product"""

    current_user = request.user

    try:
        food = mes_aliment_user(request.user.username)
        a = display_food(food)

        return render(request, 'mes_aliments.html',{"a":str(a[0][4]),
                                                   "b":str(a[1][4]),
                                                   "c":str(a[2][4]),
                                                   "d":str(a[3][4]),
                                                   "e":str(a[4][4]),
                                                   "f":str(a[5][4]),

                                                   "aa":str(a[0][0]),
                                                   "bb":str(a[1][0]),
                                                   "cc":str(a[2][0]),
                                                   "dd":str(a[3][0]),
                                                   "ee":str(a[4][0]),
                                                   "ff":str(a[5][0]),

                                                   "aaaa":"/static/img/portfolio/nutriscore/" + str(a[0][3]) + ".jpg >",
                                                   "bbbb":"/static/img/portfolio/nutriscore/" + str(a[1][3]) + ".jpg >",
                                                   "cccc":"/static/img/portfolio/nutriscore/" + str(a[2][3]) + ".jpg >",
                                                   "dddd":"/static/img/portfolio/nutriscore/" + str(a[3][3]) + ".jpg >",
                                                   "eeee":"/static/img/portfolio/nutriscore/" + str(a[4][3]) + ".jpg >",
                                                   "ffff":"/static/img/portfolio/nutriscore/" + str(a[5][3]) + ".jpg >",

                                                   "aaaaa":str(a[0][0]),
                                                   "bbbbb":str(a[1][0]),
                                                   "ccccc":str(a[2][0]),
                                                   "ddddd":str(a[3][0]),
                                                   "eeeee":str(a[4][0]),
                                                   "fffff":str(a[5][0]),
                                                    })
    except:
        message = "Veuillez remplir votre selection d'aliment de 6 produit svp =) "
        return render(request, 'error.html', {"message":message})


def replacing(request):
    """This is functionality for replace food from my food"""
    print("ouiiiiiiiiiiiiiiiiiiii")
    
    message = ''

    if request.method == "POST":
        replace_it = request.POST.getlist('remplace_food')
        print(replace_it,"555555555555555556")
        if replace_it:
            current_user = request.user
            
            liste = [[],[]]
            element = []
            c=0
            for i in replace_it:
                for j in i:
                    if j == ",":
                        c+=1
                    else:
                        liste[c].append(j)
                c+=1
            for i in liste:
                i = "".join(i)
                element.append(i)
 
            b = verification_remplacement(current_user, "".join(liste[-1]))

            if b == True:
                data_replace(request, current_user,
                             element[0], element[1])
            elif b == False:
                message = 'vous avez deja cet aliment'

        else:
            aliment = request.POST.get('rem')
            current_user = request.user
            image = image_aliment(aliment)
            titre = titre_aliment(aliment)
            a = replace(aliment)

            return render(request, 'remplacement.html', {"a":str(a[0][3]),
                                                           "b":str(a[1][3]),
                                                           "c":str(a[2][3]),
                                                           "d":str(a[3][3]),
                                                           "e":str(a[4][3]),
                                                           "f":str(a[5][3]),
                                                           
                                                           "aa":str(a[0][0]),
                                                           "bb":str(a[1][0]),
                                                           "cc":str(a[2][0]),
                                                           "dd":str(a[3][0]),
                                                           "ee":str(a[4][0]),
                                                           "ff":str(a[5][0]),
                                                           
                                                           "aaa":str(a[0][3]),
                                                           "bbb":str(a[1][3]),
                                                           "ccc":str(a[2][3]),
                                                           "ddd":str(a[3][3]),
                                                           "eee":str(a[4][3]),
                                                           "fff":str(a[5][3]),

                                                           "aaaa":"/static/img/portfolio/nutriscore/" + str(a[0][2]) + ".jpg >",
                                                           "bbbb":"/static/img/portfolio/nutriscore/" + str(a[1][2]) + ".jpg >",
                                                           "cccc":"/static/img/portfolio/nutriscore/" + str(a[2][2]) + ".jpg >",
                                                           "dddd":"/static/img/portfolio/nutriscore/" + str(a[3][2]) + ".jpg >",
                                                           "eeee":"/static/img/portfolio/nutriscore/" + str(a[4][2]) + ".jpg >",
                                                           "ffff":"/static/img/portfolio/nutriscore/" + str(a[5][2]) + ".jpg >",

                                                           "image":str(image),
                                                           "titre":str(titre),
                                                           'message':message
                                                    
                                                           })
 
    current_user = request.user
    try:
        food = mes_aliment_user(request.user.username)
        a = display_food(food)

        return render(request, 'mes_aliments.html', {"a":str(a[0][4]),
                                                       "b":str(a[1][4]),
                                                       "c":str(a[2][4]),
                                                       "d":str(a[3][4]),
                                                       "e":str(a[4][4]),
                                                       "f":str(a[5][4]),

                                                       "aa":str(a[0][0]),
                                                       "bb":str(a[1][0]),
                                                       "cc":str(a[2][0]),
                                                       "dd":str(a[3][0]),
                                                       "ee":str(a[4][0]),
                                                       "ff":str(a[5][0]),

                                                       "aaaa":"/static/img/portfolio/nutriscore/" + str(a[0][3]) + ".jpg >",
                                                       "bbbb":"/static/img/portfolio/nutriscore/" + str(a[1][3]) + ".jpg >",
                                                       "cccc":"/static/img/portfolio/nutriscore/" + str(a[2][3]) + ".jpg >",
                                                       "dddd":"/static/img/portfolio/nutriscore/" + str(a[3][3]) + ".jpg >",
                                                       "eeee":"/static/img/portfolio/nutriscore/" + str(a[4][3]) + ".jpg >",
                                                       "ffff":"/static/img/portfolio/nutriscore/" + str(a[5][3]) + ".jpg >",

                                                       "aaaaa":str(a[0][0]),
                                                       "bbbbb":str(a[1][0]),
                                                       "ccccc":str(a[2][0]),
                                                       "ddddd":str(a[3][0]),
                                                       "eeeee":str(a[4][0]),
                                                       "fffff":str(a[5][0]),
                                                       'message':message

                                                       })
    except:
        return render(request, 'mes_aliments.html')


def error(request):
    """Here we return error templace"""

    return render(request, "error.html")














