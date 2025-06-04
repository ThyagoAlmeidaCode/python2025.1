from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView #Listview - Lista os dados a partir de uma classe
from django.urls import reverse_lazy #O reverse_lazy redireciona para uma pagina
#Os arquivos precisam se conhecer
from .models import Cliente
from .forms import ClienteForm #Importa a classe do arquivo form.py

#Utilizando classes
#Classe da pagina principal
class Home(ListView):
    def get(self,request):
        return render(request, 'clientes/home_cliente.html')

#Lista os dados
class Listagem(ListView):
    #a ferramenta listview permite (model,template_name)
    model = Cliente #Conecta ao modelo de banco de dados, E Retorna uma lista chamamda cliente_list    
    template_name = 'clientes/list_cliente.html'#Conecta ao arquivo html do templates

#Classee de cadastro
class Cadastro(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/forms_cliente.html'   #Gera o template do formulario
    success_url = reverse_lazy('lista_cliente') #Redireciona para a pagina da tabela apos o cadastro

#Classe para editar os dados
class Editar(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/forms_cliente.html'
    success_url = reverse_lazy('lista_cliente')