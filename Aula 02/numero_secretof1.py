print(15*"-")
print("Descubra o valor Secreto")
print(15*"-")
print("")

numero_secreto = 10
palpite =  int(input("Informe seu palpite: "))

if numero_secreto == palpite:
    print("Parabéns!! Você acertou!!!")
elif numero_secreto > palpite:
    print("Você errou. O numero secreto é maior que seu palpite")
elif numero_secreto < palpite: 
    print("Você errou. O numero secreto é menor que seu palpite")
else: 
    print("Valor invalido!")