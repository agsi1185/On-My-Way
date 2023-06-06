from django.shortcuts import render
from .forms import new_ride_form
from django.http import HttpResponseRedirect

# Create your views here.
def new_ride_view(request):
    context = {}
    form = new_ride_form(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/displayRide')

    context['form'] = form
    return render(request, "new_ride.html", context)
