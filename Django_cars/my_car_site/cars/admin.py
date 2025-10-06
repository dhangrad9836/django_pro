from django.contrib import admin
from cars.models import Car

# Register your models here.
#admin.site.register(Car)

#https://docs.djangoproject.com/en/5.2/ref/contrib/admin/# ModelAdmin/
# the convention name is modelname and Admin next to it...so here it's CarAdmin and we are extending admin.ModelAdmin
class CarAdmin(admin.ModelAdmin):
    #here we can customize the admin interface for the Car model..we can change the order of the fields
    #fields = ['year', 'brand']
    fieldsets = [
        ('TIME INFORMATION', {'fields': ['year']}), # this is a tuple...the first element is the title of the fieldset...the second element is a dictionary with a fields key and a list of fields as the value
        ('CAR INFORMATION', {'fields': ['brand']}),
    ]

# so you register the model Car with the CarAdmin class
admin.site.register(Car, CarAdmin)