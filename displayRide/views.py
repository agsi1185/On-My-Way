from django.shortcuts import render
from new_ride.models import new_ride
from django.http import HttpResponseRedirect

# Create your views here.

def displayRides(request):
    return render(request, 'display_rides.html', {"rides":new_ride.objects.all})

def displayDetails(request, id = None):
    try:
        ride = new_ride.objects.get(pk=id)
    except ValueError:  
        ride = None
    
    if (ride == None):
        return HttpResponseRedirect('/displayRide')

    return render(request, 'details.html', {"ride":ride})