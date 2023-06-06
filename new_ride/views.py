from django.shortcuts import render
from .forms import new_ride_form

# Create your views here.
def new_ride_view(request):
    context = {}
    if request.method == "POST":
        context['form'] = new_ride_form(request.POST)
        if context['form'].is_valid():
            new_ride = context['form'].save()

    return render(request, "new_ride.html", context)
