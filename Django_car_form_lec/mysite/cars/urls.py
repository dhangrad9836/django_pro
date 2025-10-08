from django.urls import path
from . import views

# this is cars/urls.py .......this how we link the views to urls.py
app_name = 'cars'

urlpatterns = [
    path('rental_review/', views.rental_review, name= 'rental_review'),
    path('thank_you/', views.thank_you, name= 'thank_you'),   
    
]