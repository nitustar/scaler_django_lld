from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def blog(request):
    return HttpResponse("<h1>Hello, I am here with my blog!</h1><br><hr>")
