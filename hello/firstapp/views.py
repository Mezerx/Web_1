from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , HttpResponsePermanentRedirect


# Create your views here.

def index(request):
    return HttpResponse("Index")

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponseRedirect("/about")

def details(reqest):
    return HttpResponseRedirect('/')