from cProfile import label

from django import forms



class UserForm(forms.Form):
   name = forms.CharField(label="Имя клиента",min_length=3)
   age = forms.IntegerField(label="Возраст клиента",min_value=1,max_value=100)

