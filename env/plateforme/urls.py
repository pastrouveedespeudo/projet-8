from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

from django.conf.urls import handler404
from django.conf.urls import handler500

from .views import home
from .views import mention

from accounts.views import login_view
from accounts.views import register_view
from accounts.views import logout_view
from accounts.views import my_account

from mes_aliments.views import my_food
from mes_aliments.views import searching
from mes_aliments.views import food_det
from mes_aliments.views import replacing
from mes_aliments.views import error



from plateforme import views


handler404 = "plateforme.views.handler404"
handler500 = "plateforme.views.handler500"

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('mention', mention, name='mention'),
    
    path('accounts/login/', login_view, name='login_view'),
    path('accounts/register_view/', register_view, name='register_view'),    
    path('accounts/logout_view/', logout_view, name='logout_view'),
    path('accounts/mon_compte/', my_account, name='mon_compte'),

    path('mes_aliments/mes_aliments/', my_food, name='mes_aliments' ),
    path('mes_aliments/recherche/', searching, name='recherche'),
    path('mes_aliments/recherche/aliment_det', food_det, name='aliment_det'),
    path('mes_aliments/remplacement', replacing, name='remplacement'),
    path('mes_aliments/error', error, name='error'),


  


    
]
