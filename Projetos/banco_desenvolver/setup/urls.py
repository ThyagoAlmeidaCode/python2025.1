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

<<<<<<< HEAD
from clientes.views import ( 
                            home, 
                            Cliente_ListView, 
                            Cliente_CreateView, 
                            Cliente_UpdateView,
                            BuscaCliente,
                            LogoutCliente
                            )
from conta.views import DetalheContaCPF, BuscaCPFView, LogoutCPFView

=======
<<<<<<< HEAD
from clientes.views import home, Cliente_ListView, Cliente_CreateView
from conta.views import Conta_List

=======
from clientes.views import home, Cliente_ListView, Cliente_CreateView, Cliente_UpdateView
>>>>>>> 33ad5772fcc88c08a1e146afb1abba90c6678f28
>>>>>>> 33e74af301a44671a54e2fb577fec148c5e424cc
urlpatterns = [
    path('admin/', admin.site.urls),
    
     
    path('contas/busca_cpf/', BuscaCPFView.as_view(),name='buscar_cpf_form'),
    path('contas/detalhe/<str:cpf>/', DetalheContaCPF.as_view(),name='list_contas'),
    path('logout/', LogoutCPFView.as_view(),name='logout'),
    #class
    path('', home.as_view(), name='home'),
    path('clientes/list/', Cliente_ListView.as_view(),name='list_cliente'),
    path('clientes/create/', Cliente_CreateView.as_view(),name='create_cliente'),
<<<<<<< HEAD

    path('contas/ambiente_cliente/', Conta_List.as_view(), name="Conta" )
=======
    path('clientes/update/<int:pk>', Cliente_UpdateView.as_view(),name='update_cliente'),
>>>>>>> 33ad5772fcc88c08a1e146afb1abba90c6678f28
    
    
    #Path da busca e criação da
    path('clientes/busca/', BuscaCliente.as_view(),name='search_cliente'),
    path('clientes/busca/logout/', LogoutCliente.as_view(),name='logout_cliente'),
   
    
]
