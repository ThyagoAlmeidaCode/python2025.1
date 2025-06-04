from django.shortcuts import render
from django.views.generic import ListView,CreateView #Listview - Lista os dados a partir de uma classe

#Os arquivos precisam se conhecer
from .models import Cliente
from .form import ClienteForm #Apresenta a classse do form.py ao views

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

#Vai receber os dados do formulario e vai cadastrar n obano de dados
class Cliente_Create(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/forms_cliente.html'

   