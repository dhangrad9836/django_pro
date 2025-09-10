from django.shortcuts import render

# Create your views here.
def example_html(request):
    return render(request, 'my_app/example.html')