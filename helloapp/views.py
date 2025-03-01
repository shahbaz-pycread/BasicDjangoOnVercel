from django.shortcuts import render

# Create your views here.

def homepage(requests):
    return render(requests, "helloapp/home.html")
