from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request,"flights/index.html",{"flights":Flight.objects.all()})


def flight(request, flight_id):
    print("enftro flight")
    flight = Flight.objects.get(id=flight_id)
    passengers= flight.passengers.all()
    return render(request, "flights/flight.html",
            {"flight":flight,
                "passengers":passengers,
                "non_passengers":Passenger.objects.exclude(flights=flight).all()
                }

            )

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        #Finding the passenger id from the submitted form data
        passenger_id=int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        #agrego un vuelo a determinado passenger
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight",args=(flight_id,)))

    #como hay una relacion de muchos a muchos
# Create your views here.
