from django.urls import reverse
from django.test import TestCase

from mes_aliments.models import *


class test_page_jeux(TestCase):

    def test_mes_aliments_page(self):        
        response = self.client.get(reverse('jeux'))
        self.assertEqual(response.status_code,200)

class test_image(TestCase):

    def test_image(self):
        
        cat = categorie.objects.create(id=1,
                                       name_categorie='legume')
        
        food = aliment.objects.create(name_aliment='carotte',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marché',
                                      name_brand='marché',
                                      id_categorie_id=1)

        
        liste10 = []
        liste2 = ['','htps://carotte.com']
        foodd = aliment.objects.filter(image=str(liste2[1])).all()
        for i in foodd:
            liste10.append(i.nutriscore)



        out = liste10[0]

        self.assertEqual(out, 'a')










