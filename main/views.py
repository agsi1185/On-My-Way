from django.shortcuts import render

# Create your views here.

def navbar(request, id = None):
    return render(request, "main_page.html", {})