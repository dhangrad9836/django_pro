from django.urls import path
from . import views # Import views from the current package via the views.py file

urlpatterns = [
    # Define your URL patterns here
    path('', views.list_patients, name='list_patients'),  # Example URL pattern) and we gave it a name called 'list_patients'
    
]