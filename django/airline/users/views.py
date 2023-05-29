from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
    print("solo entro a login_view")
    if request.method =="POST":
        print("entro con post")
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"users/login.html",{
                "message":"invalidad credentaial"
                }
                    )

    return render(request,"users/login.html")

def logout_view(request):
    pass

# Create your views here.
