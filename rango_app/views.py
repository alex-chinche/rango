from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'info.html')

