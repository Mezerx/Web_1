from cProfile import label

from django import forms



class UserForm(forms.Form):
    #reg_text = forms.RegexField(label="Текст", regex="^[0-9][A-F][0-9]$")
    #slug_text = forms.SlugField(label="Ввидите текст")
    #url_text = forms.URLField(label="Введите URL", help_text="Например https://www.google.com")
    #uuid = forms.UUIDField(label="Ввидите UUID", help_text="Формат xxxx-xxxx-xxxx")
    #combo_text = forms.ComboField(label="Введите URL", fields=[forms.URLField(),forms.CharField(max_length=20)])
    #file_path = forms.FilePathField(label="Выберите Файл", path="C:/Games/fallout/",allow_files="True",allow_folders="True")
    #file = forms.FileField(label="Файл")
    #image = forms.ImageField(label="Изображение")
    #date = forms.DateField(label="Введите дату")
    #time = forms.TimeField(label="Введите время")