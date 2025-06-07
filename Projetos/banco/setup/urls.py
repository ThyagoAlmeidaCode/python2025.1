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
#Importar a função de views
from clientes.views import Listagem,Home,Cadastro,Editar,Deletar

urlpatterns = [
    path('admin/', admin.site.urls),    
    
    #path da classe
    path('', Home.as_view(), name="home_banco"),
    path('cliente_tabela/', Listagem.as_view(), name="lista_cliente"),
    path('cliente_form/', Cadastro.as_view(), name="cliente_create"),
    path('cliente_editar/<int:pk>', Editar.as_view(), name="cliente_update"),
    path('cliente_deletar/<int:pk>', Deletar.as_view(), name='cliente_excluir')
    
]
