# View-Based Functionss (VBF) e View-Based classes (VBC) no Django

Neste tutorial, vamos aprender sobre dois tipos principais de vistas no Django: View-Based Functionss (VBF) e View-Based classes (VBC). Vamos manter tudo simples e direto ao ponto para facilitar o entendimento.

## View-Based Functionss (VBF)
As Funções Baseadas em Views são vistas no Django que utilizam funções do Python para lidar com as requisições HTTP e retornar respostas. Vamos ver um exemplo básico.

## Exemplo de VBF
```bash
# views.py
from django.http import HttpResponse

def minha_vista(request):
    return HttpResponse("Olá, mundo!")

```

Aqui, definimos uma função chamada minha_vista que aceita um parâmetro request e retorna uma resposta com o texto "Olá, mundo!".

## Configuração da URL
Para que esta vista funcione, precisamos configurá-la em nosso arquivo de URLs.

```bash
# urls.py
from django.urls import path
from .views import minha_vista

urlpatterns = [
    path('', minha_vista, name='minha_vista'),
]
```
Agora, quando acessarmos a URL raiz do nosso site, veremos "Olá, mundo!" como resposta.


## View-Based classes (VBC)
As Classes Baseadas em Vistas utilizam classes do Python para lidar com as requisições HTTP. Elas são mais flexíveis e reutilizáveis do que as FBVs, especialmente para vistas complexas.

## Exemplo de VBC
```bash
# views.py
from django.http import HttpResponse
from django.views import View

class MinhaVista(View):
    def get(self, request):
        return HttpResponse("Olá, mundo!")
```
Aqui, criamos uma classe chamada MinhaVista que herda da classe View do Django. Definimos um método get para lidar com requisições HTTP GET.

## Configuração da URL
Precisamos configurar esta vista no nosso arquivo de URLs.
```bash
# urls.py
from django.urls import path
from .views import MinhaVista

urlpatterns = [
    path('', MinhaVista.as_view(), name='minha_vista'),
]
```
Note que utilizamos MinhaVista.as_view() para converter nossa classe em uma vista que o Django pode usar.

## Quando Usar VBF e VBV?
1. VBF: São simples e diretas, ideais para vistas simples ou para iniciantes.
2. VBC: São mais poderosas e flexíveis, recomendadas para vistas mais complexas ou quando precisamos reutilizar código.

##Conclusão
VBFs e VBCs são maneiras de criar vistas no Django. FBVs são baseadas em funções, enquanto CBVs são baseadas em classes. Ambas têm seus próprios usos e benefícios, e escolher entre elas depende da complexidade da vista e das necessidades do projeto.