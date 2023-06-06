from django.shortcuts import render
from .forms import find_ride_form

# Create your views here.
def find_ride_view(request):
    context = {}
    form = find_ride_form(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "find_ride.html", context)