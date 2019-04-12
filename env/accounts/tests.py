"""Here we testing templates"""

from django.urls import reverse
from django.test import TestCase
from .models import *

class test_account_page(TestCase):
    """This is class test for account system"""
    
    def test_login_page(self):
        """Here we test login view"""

        response = self.client.get(reverse('login_view'))
        self.assertEqual(response.status_code,200)

    def test_register_view_page(self):
        """Here we test register template"""

        response = self.client.get(reverse('register_view'))
        self.assertEqual(response.status_code,200)

    def test_logout_view_page(self):
        """Here we testing logout template"""

        response = self.client.get(reverse('logout_view'))
        self.assertEqual(response.status_code,302)

    def test_mon_compte_page(self):
        """here we testing account template"""

        response = self.client.get(reverse('mon_compte'))
        self.assertEqual(response.status_code,302)

    def test_error_page(self):
        """Here we testing error page"""

        response = self.client.get(reverse('error'))
        self.assertEqual(response.status_code,200)

class test_account(TestCase):

    def test_data_replace(self):

        a = foodAccount.objects.create(name='jb')
        a.save()
        
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


        c = foodAccount.objects.get(name='jb')
        
        food = [c.name_aliment1, c.name_aliment2, c.name_aliment3,
            c.name_aliment4, c.name_aliment5, c.name_aliment6]
        
            
        aliment = "coca ou fanta"
        new_aliment = "eau"
        
        if c.name_aliment1 == aliment:
            c.name_aliment1 = new_aliment
            c.save()
            
        if c.name_aliment2 == aliment:
            c.name_aliment2 = new_aliment
            c.save()
            
        if c.name_aliment3 == aliment:
            c.name_aliment3 = new_aliment
            c.save()
            
        if c.name_aliment4 == aliment:
            c.name_aliment4 = new_aliment
            c.save()
            
        if c.name_aliment5 == aliment:
            c.name_aliment5 = new_aliment
            c.save()
            
        if c.name_aliment6 == aliment:
            c.name_aliment6 = new_aliment
            c.save()


        d = foodAccount.objects.get(name='jb')
        out = d.name_aliment3

        self.assertEqual(out, "eau")








































