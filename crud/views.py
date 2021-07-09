from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from crud.forms import *


def thankyou(request, id):
    if request.method == 'POST':
        pi = Accommodation.objects.get(pk=id)
        fm = AccommodationRegister(instance=pi)
        return HttpResponseRedirect('/crud/success/', {'form':fm})


def add_hotel(request):
    if request.method == 'POST':
        add = AccommodationRegister(request.POST)
        if add.is_valid():
            print('Form is Valid')
            nm = add.cleaned_data['name']
            ad = add.cleaned_data['address']
            ct = add.cleaned_data['city']
            cy = add.cleaned_data['country']
            em = add.cleaned_data['email']
            ph = add.cleaned_data['phone']
            reg = Accommodation(name=nm, address=ad, city=ct, country=cy, email=em, phone=ph)
            reg.save()
            print(nm)
            print(ad)
            print(ct)
            print(cy)
            print(em)
            print(ph)
            return HttpResponseRedirect('/crud/add/')
    else:
        add = AccommodationRegister()
        print('This is a GET request')
    hot = Accommodation.objects.all()
    return render(request, 'crud/addanddisplay.html', {'form': add, 'hote':hot})


# This function will update / edit data
def update(request, id):
    if request.method == 'POST':
        pi = Accommodation.objects.get(pk=id)
        fm = AccommodationRegister(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/crud/add/')
    else:
        pi = Accommodation.objects.get(pk=id)
        fm = AccommodationRegister(instance=pi)
    return render(request, 'crud/update.html', {'form': fm})


# This functio will delete the added data
def delete_data(request, id):
    if request.method == 'POST':
        pi = Accommodation.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/crud/add/')
