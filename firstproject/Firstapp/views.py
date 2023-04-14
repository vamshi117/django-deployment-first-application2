from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.
def display(request):
   ss = '''
    <html>
            <head>
                <title>welcome page/</title>
                <style>
                    h1{
                        color : black; width:90%;
                        background-color: aqua;
                    }
                </style>
            </head>
            <body>
            <center>
            <h1>HELLO USER !! WELOCOME TO DJANGO-APP !!! HAVE A NICE DAY.....!!!</h1>
                <hr color="brown" width="90%" />
            </center>
            </body>
      </html>
''';
   return HttpResponse(ss);


def hello(request):
   print("hello/ url is requested and hello () is called");
   ss = '''
    <html>
         <head>
             <title>HELLO USER PAGE</title>
             <style>
                 h1{
                    color : blue; width:90%;
                 }
                 h2 {
                    color : green; width:80%;
                 }
                 h3{
                    color : red; width : 70%;
                 }
                 h1,h2,h3 {
                    background-color: lightblue; 
                    boder:1px black;   
                 }
             </style>
             </head>
         <body>
             <center>
             <h1>Hello user ...!!</h1>
             <hr color="brown" width="80%" />
             <h2>Welcome to Django-App</h2>
             <hr color="brown" width="60%"/>
             <h3>Have a nice day....</h3>
             <hr color="brown" width="40%" />

            </center>
         </body>
    </html> ''';
   return HttpResponse(ss);

def senddatetime(request):
     print("dtime/ url is requested and senddatetime() is executed");
     ct = time.ctime();
     print("Client request Date and time on server ::",ct);
     ss = '''
     <html>
         <head>
              <title>DATE-TIME PAGE</title>
              <style>
                   h1 {
                        color : blueviolet; width:90%; background-color:lightgrey;
                   }
                   h2 {
                        color : chocolate; width:80%; background-color: lightblue;
                   }
                   h3 {
                        color : darkblue; width:70%; background-color: antiquewhite;
                   }

              </style>
         </head>
         <body>
              <center>
                   <h1>Welcome to Django</h1>
                   <h2>server date and time ::</h2>
                   <h3>''',ct,'''</h3>
              </center>
         </body>
     </html>''';
     return HttpResponse(ss);


def homepage(request):
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
                <h1>site cannot be reached</h1>
                <h2>connection-lost</h2>
                <h3>Enter the correct url</h3>
            </center>
        </body>
    </html>
    ''';
    return HttpResponse(ss);