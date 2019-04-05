from django.contrib import admin
from django.urls import path
from .views import login, register_view, mon_compte

urlpatterns = [
    path('/login', login),
    path('/register_view', register_view),
    path('/logout_view', logout_view),
    path('/mon_compte', my_account),
    ]
