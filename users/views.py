from django.shortcuts import render
from django.http import HttpResponse

def cadastre(request):
    return render(request, 'users/cadastre.html')
