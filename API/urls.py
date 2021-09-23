from django.urls import path
from API import views

urlpatterns = [
    path('register', views.registration,name='registration'),
]