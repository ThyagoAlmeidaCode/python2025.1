from cliente import Cliente
from conta_corrente import Conta


cliente1 = Cliente("Ana Silva", "123.456.789-00")
conta1 = Conta(cliente1, "001-1", 100.00)

cliente2 = Cliente("Pedro Souza", "987.654.321-11")
conta2 = Conta(cliente2, "002-5")

conta1.exibir_dados_conta()
conta1.depositar(50.00)
conta1.sacar(20.00)
conta1.exibir_saldo()

print("\n")
conta2.exibir_dados_conta()
conta2.depositar(200.00)
conta2.sacar(300.00)
conta2.exibir_saldo()