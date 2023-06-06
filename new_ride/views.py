from django.shortcuts import render
from .forms import new_ride_form

# Create your views here.
def new_ride_view(request):
    context = {}
    form = new_ride_form(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "new_ride.html", context)
