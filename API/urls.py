from django.urls import path
from API.views import *

urlpatterns = [
    path('register',registration),
    path('user/',GetUser),
]

urlpatterns += [
    path('api/token/', CustomAuthToken.as_view())
]