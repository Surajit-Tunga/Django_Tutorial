from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path ("", views.index, name='home'), #blank path send req. to index function of views in myapp
    path ("about", views.about, name='about'),
    path ("services", views.services, name='services'),
    path ("contact", views.contact, name='contact')
]