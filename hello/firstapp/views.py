from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


# Create your views here.

def index(request):
    userform = UserForm(field_order=["age","name"])
    return render(request, 'firstapp/index.html', {'form': userform})






def about(request):
    return HttpResponse("About")