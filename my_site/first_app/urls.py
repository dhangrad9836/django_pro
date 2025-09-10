# this helps us connect to the views file
from django.urls import path
from . import views

# urlpatterns = [
#     path("sports", views.sports_view),
#     path("finance", views.finance_view),
# ]  # this is the url path we use to access the app on the browser)]


# so we will now use the news_view function to dynamically render views based on the articles dictionary
# also we used a path converter of str:topic
# <str:topic> to capture the topic from the url and pass it to the news_view function as a parameter
urlpatterns = [
    path("<int:num_page>", views.num_page_view),
    path("<str:topic>", views.news_view),
    # path("<int:num1>/<int:num2>", views.add_view),
]  # this is the url path we use to access the app on the browser)]
