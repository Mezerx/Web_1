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
    #date_time = forms.DateTimeField(label="Введите дату и время")
    #tima_delt = forms.DurationField(label="Введите промежуток времени")
    #date_time = forms.SplitDateTimeField(label="Введите дату и время")
    #number = forms.IntegerField(label="Введите целое число")
    #decimal = forms.DecimalField(label="Введите десятичное число",decimal_places=2)
   #num = forms.FloatField(label="Введите число",min_value=0,max_value=3)
   #ling = forms.ChoiceField(label="Выберите язык",choices=((1,"Английский язык"),(2,"Немецкий"),(3,"Итальянский язык")))
    #city = forms.TypedChoiceField(label="Выберите город",empty_value=None,choices=((1,"Москва"),(2,"Воронеж")))
    #country = forms.MultipleChoiceField(label="Выбирите страны",choices=((1,"Англия"),(2,"Бразилия"),(3,"Вьетнам")),help_text="Используйте CTRL")