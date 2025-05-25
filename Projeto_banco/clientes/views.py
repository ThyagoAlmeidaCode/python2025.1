from django.shortcuts import render
from django.views.generic import ListView
from .models import Cliente

class Cliente_ListView(ListView):
    model = Cliente
    template_name = 'clientes/home_cliente.html'


""" def home(request):
    return HttpResponse("<h1>Olá Mundo</h1>")

def pagina(request):
    mensagem = "Cheguei brasil"
    return render(request, 'pagina.html', {'texto': mensagem})


class pagina_dois(ListView):
    def get(self, request):
        contexto = {'mensagem': 'Clientes'}
        return render(request, 'clientes/home_cliente.html', contexto) """