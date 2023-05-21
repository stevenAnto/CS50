from django.shortcuts import render
from .models import Flight

def index(request):
    return render(request,"flights/index.html",{"flights":Flight.objects.all()})


def flight(request, flight_id):
    print("enftro flight")
    flight = Flight.objects.get(id=flight_id)
    passengers= flight.passengers.all()
    return render(request, "flights/flight.html",
            {"flight":flight,
                "passengers":passengers}

            )
    #como hay una relacion de muchos a muchos
# Create your views here.
