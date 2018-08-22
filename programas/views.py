from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    mycontext = {
    'data':'lolo'
    }
    return render(request, 'programas/index.html', context = mycontext)

def programas(request):
    mycontext={
    }
    return render(request, 'programas/programas.html', context=mycontext)
