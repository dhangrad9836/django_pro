from django.urls import path
from . import views

#add urls list here
urlpatterns = [
    path('', views.example_view)   
]