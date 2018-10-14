from django.urls import path
from django.urls import re_path
from django.views.generic import DetailView, ListView
from programas.models import Programa
from . import views

urlpatterns=[
    path('', ListView.as_view(queryset=Programa.objects.all().order_by("-title"),
    template_name="programas/index_programas.html")),
    path('programas', views.programas_todos, name= 'programas_todos'),
    re_path('(?P<pk>(\d+))',
    DetailView.as_view(model=Programa,
    template_name="programas/base_programas.html")),
    path('coaching_empresarial', views.coaching_empresarial, name='coaching_empresarial'),
    path('desarrollo_organizacional', views.desarrollo_organizacional, name='desarrollo_organizacional'),
    path('salud_empresarial', views.salud_empresarial, name="salud_empresarial")
    ]
