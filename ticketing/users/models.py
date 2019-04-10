from django.db import models
from django.contrib.auth.models import AbstractUser
import PIL

class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/", default="default.jpeg")
