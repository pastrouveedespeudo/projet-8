# projet-8

finir de revoir * re sentrainer quoi

#https://openfactfood.herokuapp.com

#Bienvenu sur notre site d'aliment, ce site a pour but de choisir des aliments depuis la database d'openfactfood. C'est un super site qui score les aliments en "nutriscore". 

Nous vous proposant de vous créer un compte et de pouvoir vous constituer un pannier de 6 aliments. Pour cela il faut que vous effectuer en prémice, une recherche depuis la page d'accueil ou depuis le menu du haut. Si un aliment ayant un nom similaire existe alors il vous sera afficher en plus de 5 autres produits sélectionner parmis les meilleur nutriscore de la catégorie. (A noter que notre database actuelle contient 3*20 produits moins ceux qui ne possèdent pas les informations suivantes : image, nutriscore, nom).

Choisir c'est aussi important ! Nous vous proposons aussi de pouvori modifier vote panier depuis "mes aliments" (la carrotte). Pour cela vous pouvez appuyer sur l'un produits. Il vous sera afficher 3 choix. Le premier est de visionner le produit directement sur OpenFactFood. Le deuxieme est de pouvoir le remplacer. Nous vous affichons encore une fois, un panel de 6 des meilleurs aliments de la catégorie. Si le produits est deja dans votre panier alors il ne sera pas ajouté une deuxieme fois ! Le troisieme choix est de réafficher le produit.  

Vous pouvez voir vos informations personnel sur Mon compte.

A noter que les css et js des pages bootstrap ne sont pas présentent

Le site est reponsif, PEP8 (pylint score de 6 a 8), les tests sont verts 

#Installer un environement virtuel.

#Installer python3.x n'oublier pas de cocher pip !!

#Installer django avec pip

#Lancer django admin-start-project

#Lancer django-admin startapp

#Lancer vos migrations apres avoir fait vos models

#Installer heroku CLI

#Creez vous un compte

#Lancer create heroku app

#Pushez le tout sur heroku depuis heroku cli (apres vous etre connecté) ou depuis github !

aliments disponibles: (sans '' ni () ni [] )

[('proactiv margarine tartine sans huile de palme 225g',), ('ravioles a poêler',), ('ferrero collection',), ('plantes et miel mille fleurs',), ('amargo 70% cacao',), ('sablés aux graines de chia',), ('fauchon',), ('mon far breton aux pruneaux',), ('2 fars bretons au lait fermier pruneaux',), ('equador',), ('farine de châtaignes',), ('carré de mie céréales',), ('cake aux ecorces de citron',), ('zingy orange matchmakers',), ('véritable petit beurre',), ('gauffrettes',), ('biscuits ptit dej bio',), ('cookies tout chocolat',), ('chocolat m. libânio ;brésil;',), ('lescargot',), ('werthers original sans sucre',), ('longue conservation nature',), ('riz thaï rouge complet',), ('riz basmati demi-complet',), ('galette de riz chocolat au lait',), ('sugar flakes',), ('pétales de maïs',), ('biscottes épidor 6 cereales',), ('pâte feuilletée pur beurre',), ('pâtes grecques',), ('corn flakes',), ('petits pains grillés',), ('nuss-frucht-mix',), ('tradition',), ('le financiers aux amandes',), ('tresor',), ('pur jus de pomme framboise',), ('raisins',), ('confiture de fraise',), ('précieux noir aromatique 75% cacao',), ('ptit-beurre tablette chocolat au lait',), ('barres céréales aux 5 céréales riz',), ('pains au lait',), ('oeufs à cacher',), ('milk mouse',), ('ravioli aux légumes',), ('céréales froot loops marshmallow',), ('confiture extra fraise 65%',), ('gnocchi à pôeler tradition',), ('mini tablette noir goût corsé',), ('biscino coeur fondant au lait',), ('sylvain spéculoos -generou',), ('roses au chocolat au lait',), ('moulages de paques',), ('farmer crunchy cornflake',)]

