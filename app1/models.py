from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=255)
    Phone = models.BigIntegerField(max_length=20)
    Email = models.EmailField(max_length=255)
    