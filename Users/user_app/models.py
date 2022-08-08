from django.db import models
from django.contrib import auth

# Create your models here.

class UserRegisterModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.username
    