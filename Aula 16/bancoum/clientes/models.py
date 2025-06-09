from django.db import models

# Create your models here.
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
