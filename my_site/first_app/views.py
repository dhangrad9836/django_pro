from django.shortcuts import render
from django.http.response import (
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    HttpResponseRedirect,
)
from django.urls import reverse

# Create your views here.


# def sports_view(request):
#     return HttpResponse("Sports Page")


# def finance_view(request):
#     return HttpResponse("Finance Page")

# so above we used function views for each type of view which can get tedious if we have many views
# so for now we will dynamically render views using a articles dictionary...we will define below the articles dictionary a single function

articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
}


# our function will be called news_view and will take in a request and topic parameter, whichh is the value in the dictionary and make sure to import Http404
def news_view(request, topic):
    # we will check if the topic is in the articles dictionary
    # we use a try/except and in the except we will return a 404 error using HttpResponseNotFound
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        # result = "No page for that topic"
        # return HttpResponseNotFound(result)
        raise Http404("404 GENEREIC ERROR")


# here we will create a view that takes in a number from the url and redirects to the corresponding topic page
# domain.com/first_app/0 will redirect to domain.com/first_app/sports
# domain.com/first_app/1 will redirect to domain.com/first_app/finance


# make sure to import HttpResponseRedirect above
def num_page_view(request, num_page):

    topics_list = list(articles.keys())  # ['sports', 'finance', 'politics']
    topic = topics_list[
        num_page
    ]  # this will get the topic based on the index passed in the url

    webpage = reverse("topic-page", args=[topic])
    return HttpResponseRedirect(webpage)  # this will redirect to the topic page


# make sure to import HttpResponse above
def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))
