from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hi(request):
    return HttpResponse("Hello World")

def watch(request):
    return HttpResponse("<h1>Latest Watch</h1>")

def home(request):
    sitename = "Motobazar"
    moto = "Best Motorcycle parts seles bazar in Bangladesh"
    return render(request, 'index.html', {'name':sitename, 'moto':moto})
