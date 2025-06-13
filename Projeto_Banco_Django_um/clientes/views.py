from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View #Listview - Lista os dados a partir de uma classe
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
     #Proibe o ascesso a pagina se nao estiver logado(sessao)
    def get(self, request, *args, **kwargs):
        #Verificar se a sessão tem 'nome_cliente'
        if 'nome_cliente' not in request.session:
            return redirect('busca_cliente') #retorna para o formulario
        
        #Se a sessao existir e o usaurio esriver autenticado segue enfrente
        return super().get(request, *args, **kwargs)

    template_name = 'clientes/list_cliente.html'#Conecta ao arquivo html do templates


#Clase de cadastro
class Cadastro(CreateView):
    model = Cliente
    def get(self, request, *args, **kwargs):
        #Verificar se a sessão tem 'nome_cliente'
        if 'nome_cliente' not in request.session:
            return redirect('busca_cliente') #retorna para o formulario
        
        #Se a sessao existir e o usaurio esriver autenticado segue enfrente
        return super().get(request, *args, **kwargs)
    form_class = ClienteForm
    template_name = 'clientes/forms_cliente.html'   #Gera o template do formulario
    
    def get_context_data(self, **kwargs):
        #**kwargs - espera qualquer argumento
        context = super().get_context_data(**kwargs) #Cria o context
        context['titulo'] = 'Cadastro de Clientes'
        context['botao'] = 'Cadastrar'
        return context
    
    success_url = reverse_lazy('lista_cliente') #Redireciona para a pagina da tabela apos o cadastro

#Classe para editar os dados
class Editar(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/forms_cliente.html'   
    
    #Deixa dinamico dados no html
    def get_context_data(self, **kwargs):
        #**kwargs - espera qualquer argumento
        context = super().get_context_data(**kwargs) #Cria o context
        context['titulo'] = 'Edição dos Clientes'
        context['botao'] = 'Editar'
        return context
    success_url = reverse_lazy('lista_cliente')

#Classe exlcuir

class Deletar(DeleteView):
    model = Cliente
    template_name = 'clientes/delete_cliente.html'
    success_url = reverse_lazy('lista_cliente')


#Trabalhando com sessoes
class BuscaCliente(View):
    #metodo que renderiza nosso formulario de autenticação
    def get(self, request):
        return render(request, 'clientes/cliente_busca_form.html')
    
    #A partir daqui vamos:
    #Identificar o email e o cpf do formulario, 
    #identificar o cliente e criar a sessao
    def post(self, request):
        email = request.POST.get('email')#Guada email digitado no formulario
        cpf = request.POST.get('cpf')#Guarda cpf digitado no formulario

        if email and cpf: #verifica se o email e cpf existem
            #Guada as informações dos clientes (nosso_cliente)
            nosso_cliente = Cliente.objects.filter(email=email, cpf=cpf).first() #Pega o primerio cliente com o email e cpf
            if nosso_cliente: 
                #Vamos criar as sessoes
                request.session['nome_cliente'] = nosso_cliente.nome
                request.session['sobrenome_cliente'] = nosso_cliente.sobrenome
                titulo = 'Cliente encontrado!'
                return render(request, 'clientes/cliente_busca_form.html',{'cliente':nosso_cliente, 'title':titulo})

            else: 
                erro_message = "Nenhum cliente encontrado."
                return render(request, 'clientes/cliente_busca_form.html', {'mensagem':erro_message})
        else: 
            erro_message = "Por favor, informe um email e cpf para consulta"
            return render(request, 'clientes/cliente_busca_form.html', {'mensagem':erro_message})
        
#Calsse que encerra a sessão
class Logout(View):
    #Metodo que verifica e encerra a sessão
    def get(self, request):
        if 'nome_cliente' in request.session:
            del request.session['nome_cliente']
        if 'sobrenome_cliente' in request.session:
            del request.session['sobrenome_cliente']

        erro_message = 'Você foi desconectado!'
        return render(request, 'clientes/cliente_busca_form.html', {'mensagem': erro_message})
        