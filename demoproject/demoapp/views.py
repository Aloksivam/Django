from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello world, this is the index view of Demoapp.")
def home(request):
    return HttpResponse("Hello world, this is the index view of Demoapp.")
# Create your views here.
