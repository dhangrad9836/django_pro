from django.shortcuts import render
from django.http.response import (
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    HttpResponseRedirect,
)
from django.urls import reverse

# Create your views here.
#the simple_view takes in a request and returns a response
def simple_view(request):
    return render(request, 'first_app/example.html') #theres some html file in my directories..so where should i point it to?