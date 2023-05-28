from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , HttpResponsePermanentRedirect


# Create your views here.

def index(request):

    return render(request, "firstapp/home.html")

def about(request):
    return HttpResponse("About")