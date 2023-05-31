from django.shortcuts import render
from django.http import *


# Create your views here.

def index(request):
    data = {"age" : 66}
    return render(request, "firstapp/index.html", context=data)

def about(request):
    return HttpResponse("About")