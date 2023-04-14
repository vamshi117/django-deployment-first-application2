from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def z11(request):
    return HttpResponse("<h1>From Myapp11 execute z11() </h1>");
def z22(request):
    return HttpResponse("<h1>From Myapp11 execute z22() </h1>")