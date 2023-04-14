from django.contrib import admin
from django.urls import path
from Myapp11 import views

urlpatterns = [
    path('aaaa/',views.z11),
    path('bbb/',views.z22),

]