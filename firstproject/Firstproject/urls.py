"""Firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from Firstapp import views
from App1 import views as v1
from App11 import views as v11
from App22 import views as v22

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.display),
    path('hello/',views.hello),
    path('dtime/',views.senddatetime),
    path('morning/',v1.f1),
    path('afternoon/',v1.f2),
    path('evening/',v1.f3),
    path('hello11/',v11.f11),
    path('datetime/',v22.f22),
    path('call1/',v1.sameurl),
    path('call2/',v1.sameurl),
    path('call3/',v1.sameurl),
    path('Myapp11/', include('Myapp11.urls')),
    path('Myapp22/', include('Myapp22.urls')),

    #re_path("^.*$",views.homepage),

]