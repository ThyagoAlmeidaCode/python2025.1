# Guia de Preparação do Ambiente Django para Projeto Bancário
Este guia irá detalhar os passos iniciais para configurar o ambiente de desenvolvimento para o seu projeto bancário utilizando Django.

### Etapa 01 - Criação e Configuração do Ambiente
Para começar, você precisará criar um ambiente virtual para o seu projeto. Isso ajuda a isolar as dependências do seu projeto de outras instalações Python no seu sistema.

### Criar o Ambiente Virtual:
Abra o seu terminal ou prompt de comando e navegue até o diretório onde você deseja criar o seu projeto. Em seguida, execute o seguinte comando:

```
python -m venv venv

```
Este comando cria uma pasta chamada venv (ou o nome que você preferir) que conterá o ambiente virtual.

### Ativar o Ambiente Virtual:
Após a criação, você precisa ativar o ambiente virtual. O comando para ativar varia ligeiramente dependendo do seu sistema operacional:

```
#No Windows:

.\venv\Scripts\activate

#No macOS/Linux:

source venv/bin/activate
```

Você saberá que o ambiente está ativado quando o nome (venv) aparecer no início da linha de comando.

### Instalar o Django:
Com o ambiente virtual ativado, instale o Django. Isso garante que o Django seja instalado dentro do seu ambiente virtual e não globalmente.

```
pip install django
```
### Criar o Projeto Django:
Agora, crie o projeto principal do Django. O nome setup é o nome do seu projeto. O ponto (.) no final é crucial, pois ele instrui o Django a criar os arquivos do projeto no diretório atual, em vez de criar uma nova subpasta com o nome do projeto.

```
django-admin startproject setup .
```
### Estrutura Inicial do Projeto
Após a criação do projeto, você notará uma estrutura de diretórios e arquivos semelhante a esta:

```
.
├── manage.py
└── setup/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
### Vamos entender brevemente o propósito de cada um:

- **manage.py**: Um utilitário de linha de comando que permite interagir com o seu projeto Django (executar o servidor, criar apps, migrar banco de dados, etc.).

- **setup/**: Este é o diretório principal do seu projeto Django.
  - **__init__.py**: Um arquivo vazio que indica ao Python que este diretório deve ser tratado como um pacote.
  - **asgi.py**: Um ponto de entrada para servidores compatíveis com ASGI (Asynchronous Server Gateway Interface), usado para aplicações assíncronas.
  - **wsgi.py**: Um ponto de entrada para servidores compatíveis com WSGI (Web Server Gateway Interface), usado para aplicações síncronas.
  - **settings.py**: Este é o arquivo de configurações do seu projeto. Ele contém todas as configurações importantes, como configurações de banco de dados, aplicativos instalados, fuso horário, etc. Você irá modificá-lo frequentemente.
  - **urls.py**: Este arquivo é onde você define o mapeamento de URLs para as views do seu projeto.


### Iniciar o Projeto
Finalmente, você pode iniciar o servidor de desenvolvimento do Django para ver seu projeto em funcionamento.

Executar o Servidor de Desenvolvimento:
No terminal, execute o seguinte comando:
```
python manage.py runserver
```
Se tudo estiver configurado corretamente, você verá uma mensagem indicando que o servidor está rodando, geralmente em http://127.0.0.1:8000/. Abra essa URL no seu navegador para ver a página de boas-vindas do Django.

Parabéns! Você concluiu a primeira etapa de preparação do ambiente para o seu projeto bancário em Django. O próximo passo seria começar a definir os modelos de dados e as views para a sua aplicação.