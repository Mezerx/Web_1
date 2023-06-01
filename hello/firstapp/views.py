from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name') # получить значение поля Имя
        age = request.POST.get('age') # получить значение поля Возраст
        output = f"<h2>Пользователь</h2><h3>Имя - {name}, " \
                 f"Возраст - {age}</h3>"
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, 'firstapp/index.html', {'form': userform})






def about(request):
    return HttpResponse("About")