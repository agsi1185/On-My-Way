from django import forms
from .models import new_ride

class new_ride_form(forms.ModelForm):

    class Meta:
        model = new_ride
        fields = ['origin', 'destination', 'seats_avail']

    # origin = forms.CharField(max_length=150)
    # destination = forms.CharField(max_length=150)
    # seats_avail = forms.IntegerField()
