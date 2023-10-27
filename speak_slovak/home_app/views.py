from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')

def slug_view(request, int_id):
    return HttpResponse(f'Hello World slug<h1>{int_id}</h1>')

def int_view(request, int_id):
    return HttpResponse(f'Hello World int<h1>{int_id}</h1>')