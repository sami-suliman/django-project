from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hi!")

def world(request):
    return HttpResponse("Hello, World!")
