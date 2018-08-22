from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name= 'index'),
    path('programas', views.programas, name= 'programas')
]
