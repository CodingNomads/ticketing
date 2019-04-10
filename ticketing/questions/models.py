from django.db import models
from users.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    replier = models.ForeignKey(User,related_name="replier", on_delete=models.CASCADE, null=True)
    date_asked = models.DateTimeField(auto_now_add=True)
    date_answered = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)