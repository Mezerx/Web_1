from cProfile import label

from django import forms



class UserForm(forms.Form):
   name = forms.CharField(label="Введите имя",help_text="Введите ФИО")
   age = forms.IntegerField(label="Введите возраст",help_text="Введите возраст")

