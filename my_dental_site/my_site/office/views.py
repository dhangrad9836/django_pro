from django.shortcuts import render
from . import models    # Import models from the current package via the models.py file

# Create your views here.
def list_patients(request):
    
    # we will fetch all patients from the database like a sql query
    all_patients = models.Patient.objects.all()  # This will fetch all Patient records from the database
    context =  {'patients':all_patients} # Create a context dictionary to pass to the template...we can now in the template reference 'patients'
    
    return render(request, 'office/list.html', context = context)  # Render the template with the context