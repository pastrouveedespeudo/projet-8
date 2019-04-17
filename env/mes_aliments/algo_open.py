"""Here we discuss with database"""


from .models import aliment
from accounts.models import foodAccount
from django.db.models.functions import Lower

def image_food(para):
    """Here we search food picture """
    try:
        try:
            food = aliment.objects.get(name_aliment__contains='{}'.format(para))
            food = aliment.objects.get(name_aliment=para)
            image = food.image
            return image
        
        except:
            para = para.split()
            food = aliment.objects.get(name_aliment__contains=str(para[0]))
            image = food.image
            return image
    except:
        pass
    
def title_food(para):
    """Here we search title picture """

    try:
        try:
            food = aliment.objects.get(name_aliment=para)
            title = food.name_aliment
            return title
        
        except:
            para = para.split()
            food = aliment.objects.get(name_aliment__contains=str(para[0]))
            title = food.name_aliment
            return title
    except:
        pass

def better_nutri(para):
    """Here we search best nutriscore from category
    from food search"""

    food = aliment.objects.get(name_aliment=para)
    food_search = [food.name_aliment, food.id_categorie_id,
                        food.nutriscore, food.image, food.id]
  
    category = aliment.objects.filter(id_categorie_id=food.id_categorie_id).order_by(
        'nutriscore')

    liste = []

    count = 0
    for i in category:
        if count == 20:
            break
        else:
            a = []
            a = [i.name_aliment, i.id_categorie_id,
                 i.nutriscore, i.image]
            liste.append(a)
    
        count += 1


    liste = liste[:6]
    liste[0] = food_search

    return liste


def food_details(value):
    """Here we calling informations about product. Thank to that we
    can redirect to Openfactfood"""

    details = aliment.objects.get(image='{}'.format(value))

    return details



def replace(para):
    """We replace food from my_food"""
  
    food = aliment.objects.get(name_aliment=para)
    food_search = [food.name_aliment, food.id_categorie_id,
                        food.nutriscore, food.image, food.id]
  
    category = aliment.objects.filter(id_categorie_id=food.id_categorie_id).order_by(
        'nutriscore')


    liste = []

    count = 0
    for i in category:
        if count == 20:
            break
        else:
            a = []
            a = [i.name_aliment, i.id_categorie_id,
                 i.nutriscore, i.image]
            liste.append(a)
    
        count += 1


    liste = liste[:6]
    liste[0] = food_search

    return liste


def data_replace(request, username, product, new_product):
    """ """   

    c = foodAccount.objects.get(name=username)
    

    food = [c.name_aliment1, c.name_aliment2, c.name_aliment3,
            c.name_aliment4, c.name_aliment5, c.name_aliment6]


    if c.name_aliment1 == product:
        c.name_aliment1 = new_product
        c.save()
        
    elif c.name_aliment2 == product:
        c.name_aliment2 = new_product
        c.save()
        
    elif c.name_aliment3 == product:
        c.name_aliment3 = new_product
        c.save()
        
    elif c.name_aliment4 == product:
        c.name_aliment4 = new_product
        c.save()
        
    elif c.name_aliment5 == product:
        c.name_aliment5 = new_product
        c.save()
        
    elif c.name_aliment6 == product:
        c.name_aliment6 = new_product
        c.save()
        


def verification_product_not_two(username, product):
    """here we check that the food is not already present"""

    c = foodAccount.objects.get(name=username)
    if c.name_aliment1 == product or c.name_aliment2  == product or\
       c.name_aliment3  == product or c.name_aliment4  == product or\
       c.name_aliment5  == product or c.name_aliment1  == product:
        return False    
    else:
        return True


def verification_replacement(username, product):
    """We verify food isnt already present""" 

    c = foodAccount.objects.get(name=username)

    food = [c.name_aliment1, c.name_aliment2, c.name_aliment3,
            c.name_aliment4, c.name_aliment5, c.name_aliment6]


    for i in food:
        if product == i:
            print("produit deja dans")
            return False
    print("pas produit deja !")
    return True

    


