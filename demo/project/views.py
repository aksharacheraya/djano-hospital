from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("hi")
def project(request):
    return HttpResponse("hello")

# Create your views here.
