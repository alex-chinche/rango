from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
    return HttpResponse("Rango says fuck you!")

def about_us(request):
    return render(request, 'info.html')

