from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Programa
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    return render(request, 'programas/index.html')

def programas_todos(request):

    return render(request, 'programas/programas_todos.html',)

def programa_individual(request):

    programa= Programa.objects.get(id__exact=id)

    return render(request, 'programas/child_programas.html', context=mycontext)

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "programas/email.html", {'form': form})

def successView(request):
    return HttpResponse('Email enviado con éxito')
