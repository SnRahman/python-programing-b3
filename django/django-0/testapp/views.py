from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Hello world!')

def index(request):
    return HttpResponse('index page')

def shop(request):
    return HttpResponse('shop page')