from django.shortcuts import render

def django_info(request):
    return render(request, 'minha_pagina/django_info.html')
