print(25*"#")
print("Descubra o numero secreto")
print(25*"#")
print("")
print(43*"#")
print("Você é capaz de descobrir o numero secreto?")
print(43*"#")

secreto_num = 12

tentativas = int(input("Quantas vezes deseja jogar? "))

for tentativa in range(1,tentativas):
    print(f"Tentativa {tentativa} de {tentativas}")
    palpite = input("Informe seu palpite: ")
    print("Seu palpite é: {}".format(palpite))
    if (secreto_num == palpite):
        print("Você acertou miseravi")
    else:
        print("Você errou miseravi")


print("Fim de jogo")