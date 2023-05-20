from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"hello/index.html")

def esteven(request):
    return HttpResponse("Helo, Esteven")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name":name.capitalize()
        })
def add(request):
    return render(request,"tasks/add.html")
# Create your views here.
