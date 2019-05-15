from django.urls import reverse
from django.test import TestCase
from .models import *
from accounts.models import *

class test_page_aliment(TestCase):

    def test_mes_aliments_page(self):        
        response = self.client.get(reverse('mes_aliments'))
        self.assertEqual(response.status_code,200)

    def test_recherche_page(self):
        response = self.client.get(reverse('recherche'))
        self.assertEqual(response.status_code,200)


    def test_aliment_det_page(self):
        response = self.client.get(reverse('aliment_det'))
        self.assertEqual(response.status_code,200)

        
    def test_remplacement_page(self):
        response = self.client.get(reverse('remplacement'))
        self.assertEqual(response.status_code,200)

        
class test_aliment(TestCase):
    
    def test_categorie(self):
        cat = categorie.objects.create(name_categorie='legume')

        category_name = categorie.objects.get(id=1)
        out = category_name.name_categorie
        out1 = category_name.id
        
        self.assertEqual(out, 'legume')
        self.assertEqual(out1, 1)

        
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
        
        food_search = aliment.objects.get(name_aliment='carotte')
        out = food_search.image

        self.assertEqual(out, 'htps://carotte.com')





    def test_title(self):
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



        out = food.name_aliment
        self.assertEqual(out, 'carotte')


    def test_better_nutri(self):
        
        cat = categorie.objects.create(id=1,
                                       name_categorie='legume')
        
        food1 = aliment.objects.create(name_aliment='carotte',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)
        
        food2 = aliment.objects.create(name_aliment='tomate',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)

        food3 = aliment.objects.create(name_aliment='olive',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)

        food4 = aliment.objects.create(name_aliment='epinard',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)



        food5 = aliment.objects.create(name_aliment='cassoulet',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)



        food6 = aliment.objects.create(name_aliment='champignon',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)


        liste = [food1.name_aliment, food1.code_product_food,
                 food1.description, food1.nutriscore, food1.image,
                 food1.name_store, food1.name_brand, food1.id_categorie_id,
                 food2.name_aliment, food2.code_product_food,
                 food2.description, food2.nutriscore, food2.image,
                 food2.name_store, food2.name_brand, food2.id_categorie_id,
                 food3.name_aliment, food3.code_product_food,
                 food3.description, food3.nutriscore, food3.image,
                 food3.name_store, food3.name_brand, food3.id_categorie_id,
                 food4.name_aliment, food4.code_product_food,
                 food4.description, food4.nutriscore, food4.image,
                 food4.name_store, food4.name_brand, food4.id_categorie_id,
                 food5.name_aliment, food5.code_product_food,
                 food5.description, food5.nutriscore, food5.image,
                 food5.name_store, food5.name_brand, food5.id_categorie_id,
                 food6.name_aliment, food6.code_product_food,
                 food6.description, food6.nutriscore, food6.image,
                 food6.name_store, food6.name_brand, food6.id_categorie_id,
                 ]

        out = liste
        self.assertEqual(out, (['carotte', '4649849',
                               'caroote','a','htps://carotte.com',
                               'marche', 'marche',1,
                               'tomate', '4649849', 'caroote',
                               'a','htps://carotte.com', 'marche', 'marche',
                               1,'olive', '4649849', 'caroote',
                               'a','htps://carotte.com', 'marche', 'marche',
                               1,'epinard', '4649849', 'caroote',
                               'a','htps://carotte.com', 'marche', 'marche',
                               1,'cassoulet', '4649849', 'caroote',
                               'a','htps://carotte.com', 'marche', 'marche',
                               1,'champignon', '4649849', 'caroote',
                               'a','htps://carotte.com', 'marche', 'marche',
                               1]

                            ))



    def test_food_details(self):
                
        cat = categorie.objects.create(id=1,
                                       name_categorie='legume')
    

        food = aliment.objects.create(name_aliment='champignon',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://champi.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)

        
        out = food.image
        self.assertEqual(out, 'htps://champi.com')



    def test_replace(self):
        
        cat = categorie.objects.create(id=1,
                                       name_categorie='legume')
    

        food1 = aliment.objects.create(name_aliment='carotte',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)
        
        food2 = aliment.objects.create(name_aliment='tomate',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)

        food3 = aliment.objects.create(name_aliment='olive',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)

        food4 = aliment.objects.create(name_aliment='epinard',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)



        food5 = aliment.objects.create(name_aliment='cassoulet',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)


        food6 = aliment.objects.create(name_aliment='champignon',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://champi.com',
                                      name_store='marche',
                                      name_brand='marche',
                                      id_categorie_id=1)


        

        liste = []

        food = aliment.objects.get(name_aliment='carotte')
        aliment_recherché = [food.name_aliment, food.id_categorie_id,
                            food.nutriscore, food.image, food.id]

        category = aliment.objects.filter(id_categorie_id=food.id_categorie_id)
        
        for i in category:
            
            a = []
  
            a = [i.name_aliment, i.id_categorie_id,
                 i.nutriscore, i.image]
            
            liste.append(a)



        liste = liste[:6]
        liste[0] = aliment_recherché

        out = liste

        self.assertEqual(out, [['carotte', 1,'a','htps://carotte.com',10],
                               ['cassoulet', 1,'a','htps://carotte.com'],
                               ['epinard',1,'a','htps://carotte.com'],
                               ['olive', 1,'a','htps://carotte.com'],
                               ['tomate',1,'a','htps://carotte.com'],
                               ['carotte',1,'a','htps://carotte.com']]

                            )

    

    def test_page_mes_aliments(self):




        
        a = foodAccount.objects.create(name='jb')
        
        a.name_aliment1='marshmallow'
        a.save()
        
        a.name_aliment2='dragibus'
        a.save()
        
        a.name_aliment3='coca ou fanta'
        a.save()
        
        a.name_aliment4='ice tea !!'
        a.save()
        
        a.name_aliment4='salade'
        a.save()
        
        a.name_aliment4='chien'
        a.save()
        
        a.name_aliment6='pomme pour se sentir non coupable'
        a.save()



        
        response = self.client.get(reverse('mes_aliments'))
        self.assertEqual(response.status_code,200)











        













