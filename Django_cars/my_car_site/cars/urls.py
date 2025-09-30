from django.urls import path
from . import views

# app_name is used for namespacing our urls
app_name = 'cars'

#create the url patterns here ..... remember it's a list
urlpatterns = [
    # remember our path function takes 3 arguments
    # 1. the url pattern as a string...ie 'list/' ...basically in the url domain.com/list/   the /list/ part
    # 2. the view function that will be called
    # 3. the name of the url pattern
    path('list/', views.list, name = 'list'),
    path('add/', views.add, name = 'add'),
    path('delete/', views.delete, name = 'delete'),
]