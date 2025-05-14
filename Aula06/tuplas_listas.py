#Criação de tupla de um unico elemento
minha_tupla = ("",)
print(type(minha_tupla))

#Tentando alterar o elemento de um tupla
segunda_tupla = (1,2,3)
#segunda_tupla[0] = 5
print(segunda_tupla[0])

#Tentando alterar o valor da tupla
""" nome = input("Informe seu nome: ")
cadastro = (nome,)
print(cadastro[0]) """

#Eganamos a tupla parte 2:
""" nome_titular = input("Informe o nome do titular: ")
saldo = float(input("Quanto quer depositar? "))
conta = (nome_titular,[saldo]) 

print(conta) """

#Engamamos a tupla parte 3
terceira_tupla = ("Dia", [25,32])
print(f"Tupla original: {terceira_tupla}")

terceira_tupla[1][0] = 45
print(f"Tupla modificada: {terceira_tupla}")