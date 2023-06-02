from cProfile import label

from django import forms



class UserForm(forms.Form):
    vyb = forms.NullBooleanField(label="Вы поедете в сочи этим летом?")
