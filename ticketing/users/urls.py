from . import views
from django.urls import path
from django.contrib.auth import login, logout


app_name="users"

urlpatterns = [

    path('login/', views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
    path('profile/', views.userprofile),
]
