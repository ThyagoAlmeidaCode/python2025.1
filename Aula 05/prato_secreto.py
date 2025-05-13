#A biblioteca random escolhe coisas aleatorias 
import random
menu =  ["Lasanha","Feijoada","Churrasco","pizza","Strognoff"]
prato_secreto = random.choice(menu).lower() #Escolhe dentro do menu um prato
print(prato_secreto)
tentativas = 5

#Enfeites do jogo
print("Acerte o prato")
print(f"Voce possui {tentativas} tentativas.")
print("")
print(20*"-")

while tentativas > 0:
    adivinha = input("Digite o nome do prato que  você acha:").lower()

    if adivinha == prato_secreto: 
        print("Parabens! Você acertou!")
        break
    else:
        tentativas -= 1
        print("Você errou!")
        print("Você ainda tem: {}".format(tentativas))
        