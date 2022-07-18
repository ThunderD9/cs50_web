from django.shortcuts import render
from django.http import HttpResponse
from urllib3 import HTTPResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")
def me(request):
    return HttpResponse("Hello, Me")