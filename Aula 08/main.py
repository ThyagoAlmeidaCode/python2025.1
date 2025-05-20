#Importa o arquivo que contem a classe contabancaria
from poo3 import ContaBancaria

conta_um = ContaBancaria("Marcos Palmeiras",1000)
conta_um.consulta_saldo()

conta_um.depositar(200)
conta_um.consulta_saldo()
#print(f"Titular da conta: {conta_um.titular}")
