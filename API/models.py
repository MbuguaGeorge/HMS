from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(('password'), max_length=128, help_text=("use'[algo]$[salt]$[hexdigest]'"))
    phone = models.IntegerField(unique=True, default=72835215)
    identification = models.IntegerField(unique=True, default=36827354)
    thumbnail = models.ImageField(blank=True)

    def __str__(self):
        return self.username