from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'country', 'email', 'phone']