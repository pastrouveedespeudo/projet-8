from django.contrib import admin
from django.urls import path
from .views import mes_aliments
from .views import recherche
from .views import aliment_det
from .views import recherche2
from .views import remplacement
from .views import error

urlpatterns = [
    path('/mes_aliments', mes_aliments),
    path('/recherche', recherche),
    path('/aliment_det', aliment_det),
    path('/recherche2', recherche2),
    path('/remplacement', remplacement),
    path('/error', error),

    ]
