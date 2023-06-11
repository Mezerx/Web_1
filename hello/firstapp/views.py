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

#изменение данных в бд
def edit(request,id):
    try:
        person = Person.objects.get(id=id)
        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")

#удаление данных из бд
def delete(request,id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")




def about(request):
    return HttpResponse("About")