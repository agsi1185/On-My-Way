from django import forms
from .models import find_ride

class find_ride_form(forms.ModelForm):

    class Meta:
        model = find_ride
        fields = "__all__"
