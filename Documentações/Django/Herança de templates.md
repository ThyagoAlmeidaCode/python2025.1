# Tutorial sobre Herança de Template no Django
A herança de templates no Django é uma poderosa ferramenta que permite reutilizar partes do seu código HTML, facilitando a manutenção e a organização do projeto. Vamos entender como isso funciona com um exemplo simples.

## O que é Herança de Template?
A herança de template permite criar uma estrutura base para o seu HTML e, em seguida, estender essa estrutura em outros templates. Isso é útil para manter uma aparência consistente em várias páginas do seu site.

## Passo a Passo
1. Crie um Template Base

Primeiro, vamos criar um template base que será a estrutura principal para as outras páginas. Crie um arquivo chamado base.html na pasta templates do seu projeto Django.

```bash
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Meu Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Bem-vindo ao Meu Site</h1>
    </header>
    <nav>
        <ul>
            <li><a href="/">Início</a></li>
            <li><a href="/about/">Sobre</a></li>
            <li><a href="/contact/">Contato</a></li>
        </ul>
    </nav>
    <main>
        {% block content %}
        <p>Conteúdo principal vai aqui.</p>
        {% endblock %}
    </main>
    <footer>
        <p>&copy; 2024 Meu Site</p>
    </footer>
</body>
</html>

```

Neste template base, usamos os blocos {% block title %} e {% block content %} para definir áreas que podem ser substituídas pelos templates que herdam de base.html.

2. Crie um Template que Herda do Template Base

Agora, vamos criar um template que herda de base.html. Crie um arquivo chamado index.html na mesma pasta templates.

```bash
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}Página Inicial{% endblock %}

{% block content %}
<h2>Esta é a página inicial</h2>
<p>Bem-vindo à página inicial do nosso site!</p>
{% endblock %}
```
No index.html, usamos {% extends "base.html" %} para dizer que este template herda do base.html. Em seguida, substituímos o conteúdo dos blocos title e content com conteúdo específico para a página inicial.

3. Crie Outras Páginas Usando a Mesma Estrutura

Podemos criar outras páginas usando a mesma estrutura. Por exemplo, crie um arquivo chamado about.html.
```bash
<!-- templates/about.html -->
{% extends "base.html" %}

{% block title %}Sobre Nós{% endblock %}

{% block content %}
<h2>Sobre Nós</h2>
<p>Saiba mais sobre nossa empresa.</p>
{% endblock %}

```
## Integrando com o Django
Certifique-se de que suas views estão configuradas para renderizar os templates corretos. Por exemplo, no views.py:

```bash
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
```
E no urls.py
```bash
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]

```
## Conclusão
A herança de templates no Django ajuda a manter seu código HTML organizado e fácil de manter. Você cria uma estrutura base e estende essa estrutura em outras páginas, substituindo apenas as partes que precisam ser diferentes. Isso economiza tempo e esforço, especialmente em projetos maiores.

Se você tiver dúvidas ou quiser experimentar mais, sinta-se à vontade para explorar a documentação oficial do Django sobre herança de templates.