from django.db import models
from clientes.models import Cliente
import uuid
# Create your models here.
class ContaBancaria(models.Model):
    TIPO_CONTA_CHOICES = [ # Opções para o tipo de conta
        ('CC', 'Conta Corrente'),
        ('CP', 'Conta Poupança'),
    ]

    cliente = models.ForeignKey(
        Cliente,                 # Relaciona com o Model Cliente
        on_delete=models.CASCADE, # O que fazer se o cliente for excluído: exclui a conta
        related_name='contas'    # Nome para acessar as contas a partir do cliente (ex: cliente.contas.all())
    )
    
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Saldo inicial 0    
    tipo_conta = models.CharField(max_length=2, choices=TIPO_CONTA_CHOICES, default='CC')
    data_criacao = models.DateTimeField(auto_now_add=True) # Data e hora da criação (preenchido automaticamente)
    ativa = models.BooleanField(default=True) # Indica se a conta está ativa

    def __str__(self):
        # Usamos self.cliente.nome para acessar o nome do cliente relacionado
        return f"Conta {self.id} - {self.cliente.nome} {self.cliente.sobrenome}"

    class Meta:
        verbose_name = "Conta Bancária"
        verbose_name_plural = "Contas Bancárias"
        ordering = ['id'] # Ordenar por número da conta por padrão