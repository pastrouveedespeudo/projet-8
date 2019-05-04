"""This is functions for searching from database"""


from .config import DATABASE, USER, HOST, PASSWORD
from django.contrib.auth import get_user_model
from accounts.models import foodAccount

User = get_user_model()

def controle_data_food(username):
    """Here we watch if user have 6 products,
    if he has -6 we ask him to select products
    else we warned him to modify his selection"""

    c = foodAccount.objects.get(name=username)

    liste = [c.name_aliment1, c.name_aliment2, c.name_aliment3,
             c.name_aliment4, c.name_aliment5, c.name_aliment6,]
    
    number = 0
    for i in liste:
        if i != "":
            number += 1
    
    if number >= 6:
        return "nombre de produit suppérieur a 6", False
    
    else:
        return "stockage du produit possible", True


def insert_food(username, food_name):
    """He we insert food"""

    c = foodAccount.objects.get(name=username)

    print("ouiiiiiiiiiiiiiiiiiiiiiii")
    if c.name_aliment1 == "":
        c.name_aliment1 = food_name
        c.save()
        
    elif c.name_aliment2 == "":
        c.name_aliment2 = food_name
        c.save()
        
    elif c.name_aliment3 == "":
        c.name_aliment3 = food_name
        c.save()
        
    elif c.name_aliment4 == "":
        c.name_aliment4 = food_name
        c.save()
        
    elif c.name_aliment5 == "":
        c.name_aliment5 = food_name
        c.save()
        
    elif c.name_aliment6 == "":
        c.name_aliment6 = food_name
        c.save()
    
    else:
        print("trop d'aliment")

 
def verify(data, liste):
    if data == "":
        pass
    else:
        number += 1
    

def verify2(data, food_name, variable):
   
    if data == food_name:
    
        variable =  False
 

def verify3(data, food_name, variable, c, food):
    if data == "" and variable != False:
        data = '{}'.format(food_name)

        
        c.save()

        variable2 = False
    else:
        pass


def data_user(username):

    c = foodAccount.objects.get(name=username)

    liste = [c.name_aliment1, c.name_aliment2, c.name_aliment3,
             c.name_aliment4, c.name_aliment5, c.name_aliment6,]


    return liste






