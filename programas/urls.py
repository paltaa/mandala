from django.urls import path
from django.urls import re_path
from django.views.generic import DetailView, ListView
from programas.models import Programa
from . import views

urlpatterns=[
    path('', ListView.as_view(queryset=Programa.objects.all().order_by("-title"),
    template_name="programas/index_programas.html")),
    path('programas', views.programas, name= 'programas'),
    re_path('(?P<pk>(\d+))',
    DetailView.as_view(model=Programa,
    template_name="programas/base_programas.html"))
    ]
