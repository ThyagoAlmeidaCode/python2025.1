from cliente import Cliente  # Importando a classe Cliente

class Conta:
    def __init__(self, cliente, numero, saldo=0.0):
        if not isinstance(cliente, Cliente):
            raise TypeError("O cliente deve ser uma instância da classe Cliente")
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        elif valor <= 0:
            print("Valor de saque inválido.")
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo atual da conta {self.numero}: R${self.saldo:.2f}")

    def exibir_dados_conta(self):
        print(f"--- Dados da Conta ---")
        print(f"Número da Conta: {self.numero}")
        print(f"{self.cliente}")  # Utiliza o método __str__ da classe Cliente
        self.exibir_saldo()
        print("-" * 20)