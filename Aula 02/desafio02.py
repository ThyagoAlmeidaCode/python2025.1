"""
2 – Construa um programa em python que solicite ao usuário um  
valor entre 10 e 100,  caso o usuário digite  um valor menor que 10 ou maior que 100, envie uma mensagem informando que os valores são inválidos caso contrário conte de zero até o numero digitado pelo usuário

"""
valor = int(input("Informe um valor entre 10 e 100: "))
if valor < 10 or valor > 100:
    print("Valor inválido")
else:
    for i in range(valor+1):
        print(f"Contando: {i}")