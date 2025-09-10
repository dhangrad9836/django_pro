# this helps us connect to the views file
from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_view) # we need to find a function called simple_view in views.py...domain.com/first_app/
    
]