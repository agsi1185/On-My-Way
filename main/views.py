from django.shortcuts import render

# Create your views here.

def navbar(request):
    return render(request, "main_page.html", {})