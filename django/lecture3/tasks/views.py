from django import forms
from django.shortcuts import render


tasks = ["foo","bar","baz"]
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Tasks")
    priority = forms.IntegerField(label="Priorityu",min_value=1,max_value=10)

def index(request):
    return render(request,"tasks/index.html",{"tasks":tasks})
def add(request):
    #si el metodo es post, o se esta enviando. Lo que se hace es crear un nuevo formulario con toda la informacion
    #de lo que se esta enviando
    if request.method == "POST":
        #creo un nuevo formulario con toda la data
        form = NewTaskForm(request.POST)
        if form.is_valid():
            #verifico manualmente su validez 
            #toma la data que es tarea
            task=form.cleaned_data["task"]
            #lo agrego a la lista
            tasks.append(task)
        else:
            return render(request,"tasks/add.html",{"form":form})
    return render(request,"tasks/add.html",{"form":NewTaskForm()})


        # Create your views here.
