from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    place=models.TextField(default="")
    def __str(self):
        return self.username