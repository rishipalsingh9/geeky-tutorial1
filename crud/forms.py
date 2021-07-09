from django import forms
from django.forms import widgets
from .models import *
from django.core import validators


class AccommodationRegister(forms.ModelForm):
    class Meta:
        model = Accommodation
        #fields = ['name', 'address', 'city', 'country', 'email', 'phone']
        # better way to display fields is as below, in upper style you can change position, 
        # but in the below position will remain as mentioned in models.py
        fields = '__all__'
        # if you want to exclude one of the field it is possible with exclude options
        #exclude = ('country',)
        # above is example to exclude one of the field
        labels = {'name': 'Hotel Name', 'address': 'Address', 'city': 'City', 'country': 'Country',
                  'email': 'Email', 'phone': 'Phone Number'}
        error_messages = ({'name': {'required': 'Hotel Name is must'}, 'address': {'required': 'Address is required'},
                           'city': {'required': 'City is required'}, 'country': {'required': 'Country is required'},
                           'email': {'required': 'Email is required'}, 'phone': {'required': 'Phone is required'}})
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Hotel Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'})
            }
