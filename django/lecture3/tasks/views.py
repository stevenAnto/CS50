from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Tasks")

def index(request):
    print("entro index",request.session["tasks"])
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"tasks/index.html",{"tasks":request.session["tasks"]})

def add(request):
    print("entro post")
    #si el metodo es post, o se esta enviando. Lo que se hace es crear un nuevo formulario con toda la informacion
    #de lo que se esta enviando
    #si es POST entonces copiar a la list
    if request.method == "POST":
        #creo un nuevo formulario con toda la data
        form = NewTaskForm(request.POST)
        if form.is_valid():
            #verifico manualmente su validez 
            #toma la data que es tarea
            task=form.cleaned_data["task"]
            #lo agrego a la lista
            request.session["tasks"].append(task)
           # request.session["tasks"]+=[task]
            print("asi quedo la lista en add",request.session["tasks"])
            #Automaticamente refresa a la otra pagina
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{"form":form})
    # pase cualquier cosa, igual renderizar
    return render(request,"tasks/add.html",{"form":NewTaskForm()})


        # Create your views here.
