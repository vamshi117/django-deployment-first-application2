from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
    return HttpResponse('<h1> style="background-color: lightgreen" GOOD MORNING USERS ...!!! HAVE A NICE DAY</h1><hr/>');
def f2(request):
    return HttpResponse('<h2>style="background-color : lightblue" GOOD AFTERNOON USERS ...!!! HOPE YOU ARE DOING GOOD...</h2><hr />');
def f3(request):
    return HttpResponse('<h3>style="background-color : lightgrey" GOOD EVENING USERS....!!!! HOW WAS YOUR DAY</h3><hr />');

def sameurl(response):
    ss = '''
    <html>
        <head>
            <style>
                h1{
                    color : red; background-color: lightblue;
                }
                h2 {
                    color : blue; background-color: antiquewhite;
                }
                h3 {
                    color : chocolate; background-color: aqua;
                }
            </style>
        </head>
        <body>
            <center>
                <h1>Hello Friends Welcome to Django</h1>
                <h2>Im working on django project </h2>
                <h3>Good Bye Friends  Have a nice day</h3>
            </center>
        </body>
    </html>
    ''';
    return HttpResponse(ss);