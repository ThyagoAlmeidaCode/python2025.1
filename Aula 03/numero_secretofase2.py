#Inportação das bibliotecas
import random
print(18*"-")
print("|Descubra  o numero|")
print(18*"-")

#O random gera valores de forma aleatoria

#Declaração de variáveis
numero_secreto = random.randrange(10,100)
print(numero_secreto)
fichas = 0
pontos = 100

#Definido os niveis
nivel = int(input("Escolha um nível: \n1-Fácil \n2-Médio \n3-Difícil: "))
if nivel == 1:
    fichas = 30
    perdi = 10
elif nivel == 2:
    fichas = 15
    perdi = 20
elif nivel == 3:
    fichas = 5
    perdi = 50
else:
    print("Valor Inválido")

tentativa = 1
while tentativa <= fichas:
    valor_usuario = int(input("Informe um valor entre 10 e 100: "))
    
    #Verifica se o valor esta correto
    if valor_usuario < 10 or valor_usuario > 100:
        print("Valor invalido!:")
        continue #Trava o usuario dentro deste IF ate digitar um numero entre 10 e 100

    #Aqui começa
    print (f"Tentativa {tentativa} de {fichas}")
    
    if valor_usuario == numero_secreto:
        print("Prabéns!! Você Acertou!!")
        break #Encerra o jogo
    elif valor_usuario < numero_secreto: 
        pontos = pontos - perdi
        print("O valor informado é menor que o numero secreto")
    elif valor_usuario > numero_secreto:
        pontos = pontos - perdi
        print("O valor informado é maior que o numero secreto")
    else:
        print("Valor desconhecido ")  
    
    tentativa += 1

if pontos < 0:
    pontos = 0
print(f"A sua pontuação é: {pontos}")
print(f"O numero secreto é: {numero_secreto}")
print("Fim do Jogo!")