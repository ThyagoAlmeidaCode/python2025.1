from django.shortcuts import render
from django.http import HttpResponse
#Aqui vai toda nossa logica

#Função da quebra de maldição
# o request é uma solicitação de um pagina(Template)
#O httpreponse responde a solicitação(Request)

def saudacao(request):
    return HttpResponse("<h1>Ola Mundo com função</h1>")

def home(request):
    return render(request, 'clientes.html')


#Desafio criar uma função chamada home que exiba uma mensagem dizendo. "AREA DO CLIENTE"