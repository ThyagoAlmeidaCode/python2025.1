"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from clientes.views import home, Cliente_ListView, Cliente_CreateView
from conta.views import Conta_List

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #class
    path('', home.as_view(), name='home'),
    path('clientes/list/', Cliente_ListView.as_view(),name='list_cliente'),
    path('clientes/create/', Cliente_CreateView.as_view(),name='create_cliente'),

    path('contas/ambiente_cliente/', Conta_List.as_view(), name="Conta" )
    
]
