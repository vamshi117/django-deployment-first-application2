from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f11(request):
    return HttpResponse("<h1>GOOD MORNING USER ...!!! HAVE A NICE DAY!!!</h1><hr />");