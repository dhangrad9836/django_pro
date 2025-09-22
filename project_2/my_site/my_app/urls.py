from django.urls import path
from . import views

#you have to set the app_name equal to the name of the app folder...whichis my_app
#we then can use this in html files to refer to urls of this app...
# so it would be in the html file
app_name = 'my_app'

#add urls list here
urlpatterns = [
    path('', views.example_view,name= 'example'), #we place a name='example' for this url so we can refer to it in html files
    path('variable/', views.variable_view, name='variable'), #we place a name='variable' for this url so we can refer to it in html files
]