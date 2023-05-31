from django.shortcuts import render
from django.http import *


# Create your views here.

def index(request):
    cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
    return render(request, "firstapp/index.html", context={"cat": cat})

def about(request):
    return HttpResponse("About")