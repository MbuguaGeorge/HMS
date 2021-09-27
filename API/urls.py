from django.urls import path
from API import views

urlpatterns = [
    path('register', views.registration),
    path('users', views.userList.as_view())
]