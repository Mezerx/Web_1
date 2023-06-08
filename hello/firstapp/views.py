from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person


# Create your views here.
#получение данных из бд и загрузка index.html
def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})

#сохранение данных в бд
def create(request):
    if request.method == 'POST':
        klient = Person()
        klient.name = request.POST.get('name')
        klient.age = request.POST.get('age')
        klient.save()
    return HttpResponseRedirect('/')





def about(request):
    return HttpResponse("About")