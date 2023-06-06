from django.shortcuts import render
from new_ride.models import new_ride

# Create your views here.

def displayRides(request):
    return render(request, 'display_rides.html', {"rides":new_ride.objects.all})