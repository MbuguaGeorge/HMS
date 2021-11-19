from django.urls import path
from API.views import *

urlpatterns = [
    path('register',registration),
    path('users',userList.as_view()),
]

urlpatterns += [
    path('api/token/', CustomAuthToken.as_view())
]