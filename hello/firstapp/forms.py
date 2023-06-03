from cProfile import label

from django import forms



class UserForm(forms.Form):
    ip_address = forms.GenericIPAddressField(label="Ip Address",help_text="Пример формата 192.168.1.1")
