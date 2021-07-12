from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.sign_up, name='sign-up'),
    path('sign/', views.sign, name='sign-u'),
    path('register/', views.register, name='register-4-signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profileu, name='user-profile'),
    path('logout/', views.user_logout, name='user-logout'),
               ]
