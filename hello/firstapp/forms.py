from cProfile import label

from django import forms



class UserForm(forms.Form):
   name = forms.CharField(label="Введите имя",initial="username")
   age = forms.IntegerField(label="Введите возраст",initial="18")

