### Adicionar Bootstrap 
Existem dois métodos principais para usar bootstrap no seu projeto Django. Ou baixando os arquivos necessários e incluindo-os no seu projeto, ou você pode instalar o módulo bootstrap 5 no seu ambiente virtual .

Usaremos o segundo método, instalando o Bootstrap 5 no ambiente virtual.

## Instalar Bootstrap 5
O Bootstrap deve ser instalado no ambiente virtual.

Você deverá instalá-lo em um projeto existente, 
Abra a visualização de comando, navegue até a pasta do ambiente virtual e ative o ambiente virtual.
Uma vez dentro do ambiente virtual, instale o Bootstrap com este comando:

```bash

pip install django-bootstrap-v5

```

## Atualizar configurações
O próximo passo é incluir o módulo bootstrap na INSTALLED_APPS em settings.py:
Adicione a opção bootstrap com na fugura abaixo:

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
]

```

## Adicionar Bootstrap 5 ao modelo
Para usar o Bootstrap no projeto, comece inserindo algumas linhas de código no seu template html:
```bash

<!DOCTYPE html>
<html>
<head>
  <title>Titulo</title>
  {% load bootstrap5 %}
  {% bootstrap_css %}
  {% bootstrap_javascript %}
</head>
<body>

<div class="container">
  <ul class="nav bg-info">
    <li class="nav-item">
      <a class="nav-link link-light" href="/">HOME</a>
    </li>
    <li class="nav-item">
      <a class="nav-link link-light" href="/members">MEMBERS</a>
    </li>
  </ul>  
</div>
</body>
</html>

```

Como você pode ver, inserimos estas três linhas na <head> seção:

```bash

    {% load bootstrap5 %}
    {% bootstrap_css %}
    {% bootstrap_javascript %}

```

1. A primeira linha informa ao Django que ele deve carregar o módulo Bootstrap 5 neste modelo.
2. A segunda linha insere o <link>elemento com a referência à folha de estilo do bootstrap.
3. A terceira linha insere o <script>elemento com a referência ao arquivo javascript necessário.


## Agora você pode usar as classes do bootstrap em seu projeto