from itertools import product

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    objects = models.Manager()
    DoesNotExist = models.Manager

class Company(models.Model):
    name = models.CharField(max_length=30)

class Product(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    price=models.IntegerField()


#Создаем объект Company с именем Электрон
firma = Company.objects.create(name="Электрон")

#создание товара компании
firma.product_set.crete(name="Samsung",price="4200")

#отдельное создание объекта с последующим добавлением в бд
ipad = Product(name="ipad", price="3200")
#при добавлении необходимо указать параметр bulk=False
firma.product_set.add(ipad,bulk=False)


#исключает из компании все товары
#при этом товары остаются в бд и не привязаны к компании
#работает, если в зависимой модели ForeignKey(Company, null = True)
#firma.product_set.clear()


#тоже самое, только в отношении одного объекта
#ipad = Product.objects.get(name="ipad")
#firma.product_set.remove(ipad)



