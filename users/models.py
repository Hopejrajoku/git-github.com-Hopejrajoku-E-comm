from django.db import models

# Create your models here.
class Profie(models.Model):
    full_name = models.CharField(max_length = 50)
    email = models.EmailField()
    birthdate = models.DateField()