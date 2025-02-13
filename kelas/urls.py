"""
URL configuration for kelas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import produk, tambah_barang, Barang_View 

def coba1(request):
    return HttpResponse("SELAMAT DATANG DI INSTITUT ASIA")

def coba2(request):
    return render(request,'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
   # path('',coba1),
    path('',coba2),
    path('produk/',produk),
    path('add/', tambah_barang),
    path('Vbrg/',Barang_View),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('hapus/<int:id_barang>',hapus_brg,name='hapus-brg'),
]
