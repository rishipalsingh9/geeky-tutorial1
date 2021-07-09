from django.urls import path
from crud import views

urlpatterns = [
    path('add/', views.add_hotel, name='hotel'),
    #path('success/<int:id>', views.thankyou, name='success-page'),
    path('delete/<int:id>/', views.delete_data, name='delete-data'),
    path('updated/<int:id>', views.update, name='updated-data'),
]