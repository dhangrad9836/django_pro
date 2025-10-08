from django.shortcuts import render, redirect
from django.urls import reverse #reverse is used to get the url of a view by its name
from . forms import ReviewForm

# Create your views here.
def rental_review(request):
    if request.method == 'POST':
        #render the form here...basically when the user fill out the form and hits submit button
        #we will get all the data from the form using request.POST dictionary
        form = ReviewForm(request.POST)
        
        
        #we will check if the form is valid
        if form.is_valid():
            print(form.cleaned_data) # cleaned_data is a dictionary of all the data that the user has submitted in the form
            #we will redirect the user to thank you page
            return redirect(reverse('cars:thank_you'))
        
    else:
        #we will pass in the form variable (it's a dictionary of the ReviewForm class/object from forms.py)to the context variable below
        form = ReviewForm()        
    return render(request, 'cars/rental_review.html', context={'form':form})


def thank_you(request):
    return render(request, 'cars/thank_you.html')