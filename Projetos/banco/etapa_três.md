# Etapa 03 - Criando os Apps da Aplicação e os Models
Nesta etapa, você irá criar um novo aplicativo para gerenciar os clientes do seu banco e definir o modelo de dados para representar as informações dos clientes.

### Criando o App clientes
Assim como o app banco, vamos criar um app específico para a funcionalidade de clientes.

### Criar o Aplicativo clientes:
No terminal (com o ambiente virtual ativado e no diretório raiz do projeto), execute:

```
python manage.py startapp clientes
```
Isso criará uma nova pasta clientes no seu projeto.

### Registrar o App clientes:
É fundamental informar ao Django que o novo aplicativo clientes existe e deve ser reconhecido pelo projeto. Edite o arquivo settings.py (localizado em setup/settings.py) e adicione a linha 'clientes.apps.ClientesConfig' à lista INSTALLED_APPS.
```
# setup/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'banco.apps.BancoConfig',
    'clientes.apps.ClientesConfig' # Adicione esta nova linha
]
```
### Fundamentos de Banco de Dados: Tabelas e Relacionamentos
Antes de mergulharmos nos modelos do Django, é importante entender os conceitos básicos de bancos de dados relacionais:

- **Tabelas:** Pense em uma tabela como uma planilha. Ela é uma coleção de dados organizada em linhas e colunas. Cada coluna representa um atributo (como "Nome" ou "CPF"), e cada linha representa um registro individual (como um cliente específico).

- **Relacionamentos entre Tabelas:** Em um banco de dados relacional, as tabelas podem se conectar umas às outras. Por exemplo, uma tabela de "Clientes" pode se relacionar com uma tabela de "Contas Bancárias" para indicar qual cliente possui qual conta. Existem diferentes tipos de relacionamentos:

- **Um para Um (One-to-One):** Uma linha em uma tabela corresponde a exatamente uma linha em outra tabela.

- **Um para Muitos (One-to-Many):** Uma linha em uma tabela pode se relacionar com várias linhas em outra tabela (ex: um cliente pode ter várias contas).

- **Muitos para Muitos (Many-to-Many):** Várias linhas em uma tabela podem se relacionar com várias linhas em outra tabela (ex: vários clientes podem participar de vários projetos).

### O ORM do Django e Modelos de Dados
O Django utiliza um ORM (Object-Relational Mapping), que é uma técnica que permite interagir com o banco de dados usando objetos Python, em vez de escrever código SQL diretamente. Isso torna o desenvolvimento mais rápido, menos propenso a erros e mais legível.

No Django, você define a estrutura das suas tabelas de banco de dados através de Modelos (Models). Cada modelo é uma classe Python que herda de django.db.models.Model, e cada atributo dessa classe representa uma coluna na tabela do banco de dados.

### Tipos de Campos de Modelo:
O Django oferece uma variedade de tipos de campos para mapear diferentes tipos de dados do banco de dados:

- **CharField:** Para strings curtas a médias (requer max_length).

- **IntegerField:** Para números inteiros.

- **DateField:** Para datas.

- **EmailField:** Para endereços de e-mail (com validação de formato).

- **BooleanField:** Para valores booleanos (True/False).

- **TextField:** Para textos longos.

- **DateTimeField:** Para data e hora.

- **DecimalField:** Para números decimais (requer max_digits e decimal_places).

- **ForeignKey:** Para definir relacionamentos "Um para Muitos".

- **ManyToManyField:** Para definir relacionamentos "Muitos para Muitos".

- **OneToOneField:** Para definir relacionamentos "Um para Um".

### Definindo o Modelo Cliente
Agora, vamos definir o modelo Cliente no arquivo clientes/models.py. Este modelo representará a tabela de clientes no seu banco de dados.

Abra o arquivo clientes/models.py e adicione o seguinte código:
```
# clientes/models.py
from django.db import models

class Cliente(models.Model):
    # Campos que representam as colunas da tabela 'Cliente' no banco de dados
    nome = models.CharField(max_length=100) # Nome do cliente, string de até 100 caracteres
    sobrenome = models.CharField(max_length=100) # Sobrenome do cliente, string de até 100 caracteres
    cpf = models.CharField(max_length=11, unique=True) # CPF do cliente, string de 11 caracteres, deve ser único
    data_nascimento = models.DateField() # Data de nascimento do cliente
    endereco = models.CharField(max_length=200) # Endereço completo do cliente, string de até 200 caracteres
    telefone = models.CharField(max_length=20, blank=True, null=True) # Telefone do cliente, opcional (blank=True, null=True)
    email = models.EmailField(unique=True) # Email do cliente, deve ser único e formatado como email
    data_cadastro = models.DateTimeField(auto_now_add=True) # Data e hora do cadastro, preenchido automaticamente na criação

    def __str__(self):
        """
        Método que retorna uma representação amigável do objeto Cliente.
        Isso é útil no painel administrativo do Django e ao depurar.
        """
        return f"{self.nome} {self.sobrenome} ({self.cpf})"

    class Meta:
        """
        A classe Meta é uma classe interna que fornece metadados sobre o modelo.
        """
        verbose_name = "Cliente" # Nome singular amigável para o modelo no painel administrativo
        verbose_name_plural = "Clientes" # Nome plural amigável para o modelo no painel administrativo
        ordering = ['nome', 'sobrenome'] # Define a ordem padrão dos registros ao consultá-los
        # Os registros serão ordenados primeiro pelo nome, depois pelo sobrenome.
```
### Explicação da Classe Meta:

A classe Meta dentro de um modelo Django é uma classe interna que permite definir metadados sobre o modelo. Ela não cria campos no banco de dados, mas sim controla o comportamento e a aparência do modelo em certas partes do Django, como o painel administrativo e as consultas.

- **verbose_name = "Cliente":** Define um nome singular mais legível para o modelo, que será exibido no painel administrativo. Em vez de "Cliente object (1)", você verá "Cliente".

- **verbose_name_plural** = "Clientes": Define o nome plural mais legível para o modelo. No painel administrativo, a seção para este modelo será "Clientes".

- **ordering = ['nome', 'sobrenome']:** Especifica a ordem padrão em que os objetos Cliente serão retornados quando você os consultar. Neste caso, eles serão ordenados primeiramente pelo campo nome em ordem crescente, e em caso de nomes iguais, serão ordenados pelo sobrenome também em ordem crescente.

### Criar e Aplicar Migrações para o App clientes
Agora que você definiu o modelo Cliente, o Django precisa criar a tabela correspondente no banco de dados.

### Gerar Migrações para clientes:
Este comando irá inspecionar o seu novo modelo Cliente e criar um arquivo de migração específico para ele.
```
python manage.py makemigrations clientes
```
Você verá uma mensagem indicando que uma nova migração foi criada para o app clientes.

### Aplicar Migrações:
Agora, aplique essa nova migração ao seu banco de dados.
```
python manage.py migrate
```
Este comando garantirá que a tabela Cliente seja criada no seu banco de dados.

### Registrar o Modelo no Painel Administrativo
Para que você possa gerenciar os registros do modelo Cliente (adicionar, editar, excluir) através da interface de administração do Django, você precisa registrá-lo.

Abra o arquivo clientes/admin.py e adicione o seguinte código:
```
# clientes/admin.py
from django.contrib import admin
from .models import Cliente # Importa o modelo Cliente que você acabou de criar

# Registra o modelo Cliente no painel administrativo do Django
admin.site.register(Cliente)
```
### Acessar o Modelo no Painel Administrativo
Iniciar a Aplicação:
Se o seu servidor não estiver rodando, inicie-o novamente:
```
python manage.py runserver
```
### Acessar a Área de Administrador:
No seu navegador, acesse:

http://127.0.0.1:8000/admin/

Faça login com as credenciais de superusuário que você criou na Etapa 02 (admin / senac@123).

Você agora deverá ver uma nova seção chamada "Clientes" (ou o nome plural que você definiu em verbose_name_plural) na página principal do painel administrativo. Clique nela para começar a adicionar e gerenciar registros de clientes!