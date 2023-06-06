from cProfile import label

from django import forms



class UserForm(forms.Form):
   name = forms.CharField(label="Введите имя")
   age = forms.IntegerField(label="Введите возраст")

