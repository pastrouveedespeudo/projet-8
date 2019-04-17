"""Here we discuss with database for
food from user database"""


from accounts.models import *
from mes_aliments.models import *


def my_food_user(username):
    """Here we take user food"""

    liste = []
    c = foodAccount.objects.get(name=username)
    food = [c.name_aliment1, c.name_aliment2, c.name_aliment3,
            c.name_aliment4, c.name_aliment5, c.name_aliment6]
    for i in food:
        print(i)
        liste.append(i)
        
    with open("mimi.py","w") as file:
        file.write(str(liste))
        print("fait")
        print(liste)
    return food

def display_food(food_list):
    """Here we take informations food for template"""

    liste_ali = []
    try:
        for i in food_list:
             z = aliment.objects.get(name_aliment=i)
             liste = []
             liste = [z.name_aliment, z.code_product_food,
                      z.description, z.nutriscore,
                      z.image, z.name_store, z.name_brand]

             liste_ali.append(liste)
     

        return liste_ali
    
    except:
        pass
     
