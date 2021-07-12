from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            print('Form Validated')
            fm.save()
            return HttpResponseRedirect('/loginapp/signup/')
    else:
        fm = UserCreationForm()
    return render(request, 'loginapp/signup.html', {'form': fm})


'''
    Above function is for the signup using builting UserCreationForm, but it display on three
    types which are User, Password, Renter Password.. To get more options we need to create forms.py file
    lets go to forms.py and check comments there
    
    >> import form from forms.py files
    This form will allow to add other details as per your own requirment
'''

'''
Lets create a new function to display our new forms.
Messages model allow to send messages.
'''

def sign(request):
    if request.method == 'POST':
        fm = SignForm(request.POST)
        if fm.is_valid():
            print('Form Validated')
            fm.save()
            messages.success(request, 'Success. Proceed for Login')
            return HttpResponseRedirect('/loginapp/sign/')
    else:
        fm = SignForm()
    return render(request, 'loginapp/sign.html', {'form': fm})


def register(request):
    if request.method == 'POST':
        fm = SignForm(request.POST)
        if fm.is_valid():
            print('Form Validated')
            fm.save()
            messages.success(request, 'Success. Proceed for Login')
            return HttpResponseRedirect('/loginapp/sign/')
    else:
        fm = SignForm()
    return render(request, 'loginapp/register.html', {'form': fm})


'''
    Login-in-built form we will use to get hold of signup user to login to our databases
    to do so we just need to write our views after importing the login view from django
'''

# Login View Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request = request, data = request.POST)
            if fm.is_valid():
                print('Form is Valid')
                uname = fm.cleaned_data['username']
                upwd = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upwd)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully!')
                    return HttpResponseRedirect('/loginapp/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'loginapp/userlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/loginapp/profile/')


def profileu(request):
    if request.user.is_authenticated:
        return render(request, 'loginapp/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/loginapp/login/')

'''
The above dict is used to get the user name of login person to display on the web page.
There are three options either you can get user, first_name or last_name to display on the page
 >>>> is_authenticated will make sure that only user who have login id be able to login to the profile page
 now profile page will not be displayed if you are not logged in.
'''


# Logout Views

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/loginapp/login/')