from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Programa

# Create your views here.

def index(request):
    mycontext = {
    'data':'lolo'
    }
    return render(request, 'programas/index.html', context = mycontext)

def programas(request):

    return render(request, 'programas/programas.html', context=mycontext)

def programa_individual(request):

    programa= Programa.objects.get(id__exact=id)

    return render(request, 'programas/child_programas.html', context=mycontext)
