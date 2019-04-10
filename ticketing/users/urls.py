from users.views import *
from django.urls import path

urlpatterns = [
    path('login/', login),
    path('logout/', logout)
]
