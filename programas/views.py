from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Programa

#from functions import mostrarPrograma
# Create your views here.

def index(request):
    mycontext = {
    'data':'lolo'
    }
    return render(request, 'programas/index.html', context = mycontext)

def programas_todos(request):

    return render(request, 'programas/programas_todos.html',)

def programa_individual(request):

    programa= Programa.objects.get(id__exact=id)

    return render(request, 'programas/child_programas.html', context=mycontext)
