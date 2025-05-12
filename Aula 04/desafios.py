""" 
    Desafio 01: Soma dos Elementos: Dada a lista de números inteiros numeros = [10, 20, 30, 40, 50], calcule e imprima a soma de todos os seus elementos. 
"""
#Declarando a lista
numeros = [10,20,30,40,50]
caixinha_da_soma = 0
""" 
for i in range(0,10): #[0,1,2,3,4,5,6,7,8,9]
    print(i) """
for n in numeros:
    caixinha_da_soma = caixinha_da_soma + n
print(caixinha_da_soma)