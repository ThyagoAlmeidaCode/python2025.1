from django.shortcuts import render
from django.views.generic import ListView #Listview - Lista os dados a partir de uma classe

#Os arquivos precisam se conhecer
from .models import Cliente

#Utilizando classes
#Classe da pagina principal
class Home(ListView):
    def get(self,request):
        return render(request, 'clientes/home_cliente.html')


class Clientes_list(ListView):
    #a ferramenta listview permite (model,template_name)
    #Conecta ao modelo de banco de dados
    model = Cliente #retorna uma lista chamamda cliente_list

    #Conecta ao arquivo html do templates
    template_name = 'clientes/list_cliente.html'


    """ def get(self,request):
        return render(request, 'clientes/clientes_list.html') """