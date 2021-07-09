from django.db import models
from cities_light.abstract_models import (AbstractCity, AbstractCountry, AbstractRegion, AbstractSubRegion)
from cities_light.receivers import connect_default_signals

#from phonenumber_field import PhoneNumberField

# Create your models here.


class Country(AbstractCountry):
    pass


class City(AbstractCity):
    pass
    

class Region(AbstractRegion):
    pass


class SubRegion(AbstractSubRegion):
    pass


class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=15)
