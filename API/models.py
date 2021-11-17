from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework.authtoken.models import Token


# Create your models here.
class Profile(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(('password'), max_length=128, help_text=("use'[algo]$[salt]$[hexdigest]'"))
    phone = models.IntegerField(unique=True, default=72835215)
    identification = models.IntegerField(unique=True, default=36827354)
    thumbnail = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.username

#post signal for token pass reset
@receiver(reset_password_token_created)
def password_reset_token_created(sender,instance,reset_password_token,*args,**kwargs):
    email_plainttext_message="{}?token={}".format(reverse('password_reset:reset-password-request'),reset_password_token.key)
    send_mail("Password reset for {title}".format(title="Maseno HMS"),email_plainttext_message,"infotdbsoft@gmail.com",[reset_password_token.user.email])       