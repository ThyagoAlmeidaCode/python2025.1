from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from django.urls import reverse_lazy


from .models import Cliente
from .forms import ClienteForm


#Pagina inicial
class home(ListView):
    def get(self, request):
        return render(request, 'clientes/home_cliente.html')

class Cliente_ListView(ListView):
    model = Cliente
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