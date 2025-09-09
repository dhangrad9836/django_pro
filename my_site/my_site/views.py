from django.http.response import HttpResponse  # added this import


def home_view(request):
    return HttpResponse("HOME PAGE View")
