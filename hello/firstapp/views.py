from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


# Create your views here.

def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse(f"<h2>Имя введено корректно - {name}</h2>")
    return render(request, 'firstapp/index.html', {'form': userform})






def about(request):
    return HttpResponse("About")