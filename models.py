from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)