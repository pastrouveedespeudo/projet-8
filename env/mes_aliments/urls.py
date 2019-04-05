from django.contrib import admin
from django.urls import path
from .views import my_food
from .views import searching
from .views import food_det
from .views import replace
from .views import error

urlpatterns = [
    path('/mes_aliments', my_food, name='mes_aliments'),
    path('/recherche', searching, name='recherche'),
    path('/aliment_det', food_det, name='aliment_det'),
    path('/remplacement', replace, name='remplacement'),
    path('/error', error, name='error'),
    ]
