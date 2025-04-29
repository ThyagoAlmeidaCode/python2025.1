""""
    Estrutura de decisão 
    Classificação
        >Simples
        >Composta
        >Encadeada
        >Aninhada
"""
print("Decisão Simples - é dada por uma única decisão")
idade = 18

if idade >= 18:
    print("Maior de idade")

print(15*"-")

print("Composta - uma única decisão e uma reposta padrão")

if idade >= 18:
    print("Maior de idade")
else: 
    print("Infelizmete não posso te ajudar")  

print(15*"-")

print("Encadeada -é dada por mais de uma decisão e uma reposta padrão")
if idade >= 18:
    print("Maior de idade")
elif idade <= 18:
    print("Menor de idade")
else:
    print("Infelizmete não posso te ajudar") 

print(15*"-")

print("Aninhada - Possui uma estrutura de decisão dentro da outra")
classificacao = 18
ingresso = True

if classificacao >= 16:
    if ingresso == True:
        print("Voce pode assitir ao filme")
    else:
        print("Você não pode assitir ao filme")
else: 
    print("Você não pode entrar")