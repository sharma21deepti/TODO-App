from django.contrib import admin
from django.urls import path, include
from task import views

urlpatterns = [
    path('', views.task, name='task'),
    path('about', views.about, name='about'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
