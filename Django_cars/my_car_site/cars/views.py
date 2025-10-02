from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def list(request):
    # retrieve all car objects from the database and store them in a all_cars variable
    all_cars = models.Car.objects.all()
    
    # store them in a dictionary in a context variable which the variable name is all_cars
    context = {'all_cars': all_cars}
    
    # pass the context variable to the template
    return render(request, 'cars/list.html', context=context)

def add(request):
    # we are going to add an if statement here later to handle the form submission
    if request.POST:
        brand =  request.POST['brand']  # we are getting the value of the brand input field...this is b/c of the POST..so POST is a dictionary
        year = int(request.POST['year']) # we are getting the value of the year input field
        models.Car.objects.create(brand=brand, year=year) # create a new Car object and save it to the database
        # if user submitted new car ---> redirect them to the list page
        return redirect(reverse('cars:list'))
    
    else:
        # if user just came to the add page ---> show them the add page if the user does not submit the form    
        return render(request, 'cars/add.html')

def delete(request):
    # we are going to add an if statement here later to handle the form submission
    if request.POST:
        # delete the car
        pk = request.POST['pk'] # get the primary key of the car to be deleted and store it in a pk variable
        try:
            models.Car.objects.get(pk=pk).delete() # get the car object with the primary key pk and delete it
            return redirect(reverse('cars:list')) # redirect the user to the list page
        except:
            print("Car with primary key", pk, "does not exist")
            return render(request, 'cars/delete.html')
    else:
        # if user just came to the delete page ---> show them the delete page if the user
        return render(request, 'cars/delete.html')