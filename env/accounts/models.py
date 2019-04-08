from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class food_account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_aliment = models.CharField(max_length=100)


    @receiver(post_save, sender=User)
    def create_food_account(sender, instance, created, **kwargs):
        if created:
            food_account.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_food_account(sender, instance, **kwargs):
        instance.food_account.save()
