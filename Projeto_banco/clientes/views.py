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


class BuscaCPFView(View):
    template_name = 'clientes/busca_cpf_form.html'

    def get(self, request):
        # Renderiza o formulário
        return render(request, self.template_name)

    def post(self, request):
        # Este método 'post' não será usado diretamente com o `method="get"` no HTML
        # mas é bom tê-lo se você mudar de ideia para usar POST.
        # Por enquanto, o formulário envia via GET.
        return render(request, self.template_name)
        #pass