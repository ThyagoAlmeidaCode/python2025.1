from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Cliente
from .forms import ClienteForm
from django.urls import reverse_lazy
from conta.models import ContaBancaria

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
    form_class = ClienteForm
    
    template_name = 'clientes/forms_cliente.html'
    success_url = reverse_lazy('list_cliente')
    paginate_by = 2 # Define 10 itens por página
    