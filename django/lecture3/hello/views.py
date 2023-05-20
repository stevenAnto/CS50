from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello")

def esteven(request):
    return HttpResponse("Helo, Esteven")

def greet(request, name):
    return HttpResponse(f"Hello, {name}")

# Create your views here.
