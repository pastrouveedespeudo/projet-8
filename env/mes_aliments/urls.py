from django.contrib import admin
from django.urls import path
from .views import mes_aliments
from .views import recherche
from .views import aliment_det
from .views import remplacement
from .views import error

urlpatterns = [
    path('/mes_aliments', mes_aliments, name='mes_aliments'),
    path('/recherche', recherche, name='recherche'),
    path('/aliment_det', food_det, name='aliment_det'),
    path('/remplacement', remplacement, name='remplacement'),
    path('/error', error, name='error'),

    ]
