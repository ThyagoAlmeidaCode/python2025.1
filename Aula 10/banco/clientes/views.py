from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
#Aqui vai toda nossa logica

#Função da quebra de maldição
# o request é uma solicitação de um pagina(Template)
#O httpreponse responde a solicitação(Request)

def saudacao(request):
    return HttpResponse("<h1>Ola Mundo com função</h1>")

def home(request):
    return render(request, 'clientes.html')


class pagina_dois(ListView):
    def get(self, request):
        contexto = {'mensagem': 'Olá, mundo com classe!'}
        return render(request, 'paginadois.html', contexto)