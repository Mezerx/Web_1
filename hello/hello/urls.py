from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstapp import views


urlpatterns = [
    path('',views.index),
    re_path(r'^about',views.about),
    re_path(r'^contact', views.contact),
    #re_path(r'^products/$', views.products), # маршрут по умолчанию
    #re_path(r'^products/(?P<productid>\d+)/', views.products),
    #re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    path('products/<int:productid>/', views.products),
    path('users/<int:id>/<str:name>/', views.users),
    path('products/', views.products),# маршрут по умолчанию
    path('users/', views.users),# маршрут по умолчанию
]
