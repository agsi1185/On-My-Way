"""
URL configuration for omw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from new_ride import views
from main import views as navbar_view
from find_ride import views as findRideView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', navbar_view.navbar, name = "main_page_view"),
    path('new_ride_register/', views.new_ride_view, name = "new_ride_view"),
    path('find_ride_search/', findRideView.find_ride_view, name = "find_ride_view")
]
