from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Cliente

#Pagina inicial
class home(ListView):
    def get(self, request):
        return render(request, 'clientes/home_cliente.html')


class Cliente_ListView(ListView):
    model = Cliente
    template_name = 'clientes/list_cliente.html'