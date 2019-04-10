from django.urls import path, include
from django.contrib import admin

from clientes.views import ClienteList


urlpatterns = [
    path('lista/clientes/' , ClienteList.as_view() , name='lista_clientes'),


    ]