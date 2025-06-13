from django.shortcuts import render
<<<<<<< HEAD
from django.urls import reverse_lazy


from django.views.generic import View,DetailView # Importe TemplateView e ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import transaction # Para garantir que as operações financeiras sejam seguras
from decimal import Decimal # Para trabalhar com dinheiro de forma precisa
from django.contrib import messages # Para mostrar mensagens ao usuário

from .models import ContaBancaria, Cliente
# Create your views here.

class DetalheContaCPF(DetailView):
    model = ContaBancaria
    context_object_name = 'contas'
    template_name = 'conta/list_conta.html'

    def get_object(self, queryset=None):
            cpf = self.kwargs.get('cpf')          
            return get_object_or_404(ContaBancaria, cliente__cpf=cpf)
    

class BuscaCPFView(View):
    def get(self, request, *args, **kwargs):
        # Exibe o formulário de busca
        return render(request, 'conta/busca_cpf.html')

    def post(self, request,*args, **kwargs):
        # Processa a submissão do formulário
        cpf = request.POST.get('cpf') # Pega o valor do campo 'cpf' do formulário

        if cpf:
            cliente = Cliente.objects.filter(cpf=cpf).first()
            
            if cliente: # Se um cliente foi encontrado (CPF existe)
                # 2. Armazena o CPF e o NOME do cliente na sessão
                request.session['cpf_logado'] = cpf
                request.session['nome_cliente_logado'] = cliente.nome # Adapte 'nome_completo' para o campo correto do seu modelo Cliente

                messages.success(request, f"CPF {cpf} validado com sucesso!")
                # 3. Redireciona para a página de detalhes da conta
                return redirect(reverse('list_contas', kwargs={'cpf': cpf}))
            else:
                
                # CPF não encontrado
                messages.error(request, "CPF não encontrado. Por favor, verifique e tente novamente.")
        else:
            # CPF não digitado
            messages.error(request, "Por favor, informe um CPF.")

        # Se houver erro, renderiza o formulário novamente com a mensagem de erro
        return render(request, 'conta/busca_cpf.html')
    
class LogoutCPFView(View):
    def get(self, request, *args, **kwargs):
        # Remove o CPF e o nome do cliente da sessão
        if 'cpf_logado' in request.session:
            del request.session['cpf_logado']
        if 'nome_cliente_logado' in request.session: # Remove o nome também
            del request.session['nome_cliente_logado']

        messages.info(request, "Você foi desconectado.")
        return redirect('buscar_cpf_form')
=======
from django.views.generic import ListView,CreateView

from .models import ContaBancaria
# Create your views here.

class Conta_List(ListView):
    model = ContaBancaria
    template_name = "contas/ambiente_conta.html"
>>>>>>> 33e74af301a44671a54e2fb577fec148c5e424cc
