
from django.urls import path, include
from . import views

app_name="questions"

urlpatterns = [

    path('', views.completed, name="completed"),
    path('', views.pending_questions, name="pending_questions")

]
