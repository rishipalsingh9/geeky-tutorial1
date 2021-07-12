from django.db import models

class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=15)
