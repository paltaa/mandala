from django.urls import path
from django.urls import re_path
from django.views.generic import DetailView, ListView
from programas.models import Programa
from . import views

urlpatterns=[
    path('',
    ListView.as_view(queryset=Programa.objects.all().order_by("-title"),
    template_name="programas/index_programas.html"),
    name="home"),

    path('programas',
    ListView.as_view(queryset=Programa.objects.all().order_by("-title"),
    template_name="programas/programas_todos.html"),
    name= 'programas_todos'),

    re_path('(?P<pk>(\d+))',
    DetailView.as_view(model=Programa,
    template_name="programas/base_programas.html")),

    path('coaching_empresarial',
    ListView.as_view(queryset=Programa.objects.all().order_by("-title"),
    template_name='programas/coaching_empresarial.html'),
    name='coaching_empresarial'),

    path('desarrollo_organizacional',
    ListView.as_view(queryset=Programa.objects.all().order_by("-title"),
    template_name='programas/desarrollo_organizacional.html'),
    name='desarrollo_organizacional'),

    path('salud_empresarial',
    ListView.as_view(queryset=Programa.objects.all().order_by("-title"),
    template_name='programas/salud_empresarial.html'),
    name="salud_empresarial"),
    ]
