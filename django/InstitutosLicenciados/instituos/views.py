from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Esta sera una pagina de institutos")

# Create your views here.
