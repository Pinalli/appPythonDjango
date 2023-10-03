from django.urls import path
from django.shortcuts import render

def cadastre(request):
    if request.method == "GET":
        return render(request, 'cadastre.html')

