from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from firstapp import views


urlpatterns = [
    path('',views.index),
    path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
    path('contact/',TemplateView.as_view(template_name="firstapp/contact.html",extra_context= {"work":"Разработка программных продуктов"})),


]
