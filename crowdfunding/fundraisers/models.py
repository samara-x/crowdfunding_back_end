from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import timezone
from datetime import timedelta


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    

class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_fundraisers'
    )

class Pledge(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)
    fundraiser = models.ForeignKey(
        'Fundraiser',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )

#I have chosen to not allow anonymous pledges
#have kept this in as an option to change in the future if needed. 