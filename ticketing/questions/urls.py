from django.urls import path
from . import views


app_name="questions"

urlpatterns = [
    path('', views.pending_questions, name="pending_questions"),
    path('completed', views.completed, name="completed"),
]