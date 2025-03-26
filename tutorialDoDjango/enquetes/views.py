from django.shortcuts import render
from django.http import HttpResponse

# crie suas views aqui.

def index(request):
    return HttpResponse("Olá mundo. Você está no indice da enquete.")