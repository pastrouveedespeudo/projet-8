"""Here we create table for food stuff"""

from django.db import models

class categorie(models.Model):
    """we create category"""

    name_categorie = models.CharField(max_length=100)
    


class aliment(models.Model):
    """We create food table"""

    name_aliment = models.CharField(max_length=100)
    code_product_food = models.CharField(max_length=100)
    description = models.TextField()
    nutriscore = models.CharField(max_length=100)
    image = models.ImageField()
    name_store = models.CharField(max_length=100)
    name_brand = models.CharField(max_length=100)
    id_categorie = models.ForeignKey(categorie, on_delete=models.CASCADE)




class recherche(models.Model):
    """we create seaching table"""

    recherche = models.CharField(max_length=255)
            



class substitut(models.Model):
    """We create substitue tables"""

    name_aliment = models.CharField(max_length=100)
    code_product_food = models.CharField(max_length=100)
    description = models.TextField()
    nutriscore = models.CharField(max_length=100)
    image = models.ImageField()
    name_store = models.CharField(max_length=100)
    name_brand = models.CharField(max_length=100)









    
