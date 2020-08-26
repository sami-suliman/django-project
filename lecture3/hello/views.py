from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"Hello/index.html")

def world(request):
    return HttpResponse("Hello, World!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")