from django.shortcuts import render  # Adicionado - Mostrar templates
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Gustavo',
    })


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return HttpResponse('sobre')
