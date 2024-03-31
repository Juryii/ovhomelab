"import modules"
from django.shortcuts import render

# Create your views here.


def index(request):
    "return index.html"
    return render(request, 'project/index.html')
