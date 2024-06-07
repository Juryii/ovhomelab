""" импорт модулей"""
from django.shortcuts import render

# Create your views here.
def index(request):
    "return index.html"
    return render(request, "heat_networks_library/index.html")
