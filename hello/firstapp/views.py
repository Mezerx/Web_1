from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , HttpResponsePermanentRedirect


# Create your views here.

def index(request):
    header = "Персональные данные"
    langs = ["Английский","Немецкий","Испанский"]
    user = {"name" : "Максим" , "age" : 30}
    addr = ["Виноградная", 23 , 45]
    data = {"header": header , "langs" : langs, "user" : user, "addr" : addr}
    return render(request, "index.html", context=data)

def about(request):
    return HttpResponse("About")