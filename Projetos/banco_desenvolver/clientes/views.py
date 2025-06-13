from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,UpdateView,View
from django.urls import reverse_lazy
from django.contrib import messages


from .models import Cliente
from .forms import ClienteForm


#Pagina inicial
class home(ListView):
    def get(self, request):
        return render(request, 'clientes/home_cliente.html')

class Cliente_ListView(ListView):
    model = Cliente
    
    #Proibe acesso a pagina sem estar logado
    def get(self, request, *args, **kwargs):
        # Verifica se a sessão tem 'nome_usuario'
        if 'nome_cliente' not in request.session:            
            return redirect('search_cliente')  # Redireciona para a página de login se a sessão não estiver ativa
        
        # Se a sessão estiver ativa, continue com a lógica padrão da ListView
        return super().get(request, *args, **kwargs)   
    
    template_name = 'clientes/list_cliente.html'
    context_object_name = 'clientes'
    
class Cliente_CreateView(CreateView):
    model = Cliente
    template_name = 'clientes/forms_cliente.html'    
    form_class = ClienteForm 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de clientes'
        context['botao'] = 'Cadastrar'
        return context
    
    success_url = reverse_lazy('list_cliente')
    
class Cliente_UpdateView(UpdateView):
    model = Cliente    
    template_name = 'clientes/forms_cliente.html'    
    form_class = ClienteForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edição de clientes'
        context['botao'] = 'Salvar'
        return context
    
    success_url = reverse_lazy('list_cliente')
    


#Configurado acesso com section
class BuscaCliente(View):
    
    def get(self, request, *args, **kwargs):
      return render(request, 'clientes/busca_cliente_form.html')  
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        
        if email and cpf:
            clientes = Cliente.objects.filter(email=email, cpf=cpf).first()
            if clientes:
                request.session['nome_cliente'] = clientes.nome
                request.session['sobrenome_cliente'] = clientes.sobrenome
                titulo = 'Cliente Encontrado'
                return render(request, 'clientes/uno_cliente.html', {'clientes': clientes, 'titulo': titulo})
            else:
                error_message = "Nenhum cliente encontrado com o email e CPF fornecidos."
                return render(request, 'clientes/busca_cliente_form.html', {'error_message': error_message})
        else:
            error_message = "Por favor, informe um email e CPF para buscar."
            return render(request, 'clientes/busca_cliente_form.html', {'error_message': error_message})

class LogoutCliente(View):
    def get(self, request, *args, **kwargs):
        # Remove o cpf e o nome do cliente da sessão
        if 'nome_cliente' in request.session:
            del request.session['nome_cliente']
        if 'sobrenome_cliente' in request.session: # Remove o nome também
            del request.session['sobrenome_cliente']

        error_message = "Vcoe foi desconectado."
        return render(request, 'clientes/busca_cliente_form.html', {'error_message': error_message})
        