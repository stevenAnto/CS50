from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/user.html")

def login_view(request):
    print("solo entro a login_view")
    if request.method =="POST":
        print("entro con post")
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request,username=username, password=password)
        print("este es el user,",user)
        if user is not None:
            print("Usuario valido")
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            print("usuario no valido")
            return render(request,"users/login.html",{
                "message":"invalidad credentaial"
                }
                    )

    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
        "message":"Logged out"
        }
            )
    pass

# Create your views here.
