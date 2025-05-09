

import random
print(18*"-")
print("|Descubra  o numero|")
print(18*"-")

#O random gera valores de forma aleatoria

#Declaração de variáveis
numero_secreto = random.randrange(10,100)
fichas = 0
pontos = 100


#Definido os niveis
nivel = int(input("Escolha um nível: \n1-Fácil \n2-Médio \n3-Difícil: "))
if nivel == 1:
    fichas = 30
elif nivel == 2:
    fichas = 15
elif nivel == 3:
    fichas = 5
else:
    print("Valor Inválido")

tentativa = 1
while tentativa <= fichas:
    valor_usuario = int(input("Informe um valor entre 10 e 100: "))
    if valor_usuario < 10 or valor_usuario > 100:
        print("Informe um valor entre 10 e 100:")
        continue
    print (f"Tentativa {tentativa} de {fichas}")
    
    if valor_usuario == numero_secreto:
        print("Prabéns!! Você Acertou!!")
        break
    elif valor_usuario < numero_secreto: 
        print("O valor informado é menor que o numero secreto")
    elif valor_usuario > numero_secreto:
        print("O valor informado é maior que o numero secreto")
    else:
        print("Valor desconhecido ")


    

        
    tentativa += 1

print(f"Sua pontuação foi: {pontos} ")
print(f"O valor oculto era: {numero_secreto}")
print("Fim do jogo!")