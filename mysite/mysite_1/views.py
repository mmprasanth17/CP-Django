from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def page1(request):
    return HttpResponse("My name is Prasanth")

def page2(request):
    return HttpResponse("My Father Name is Mani")

def page3(request):
    return HttpResponse("My Mother Name is Roja")

