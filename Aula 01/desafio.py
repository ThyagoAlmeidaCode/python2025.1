""" Desafio """
#Crie um programa que solicite o time de futebol do usuário. 
#O programa deve gravar o nome do time em uma varável e em seguida exibir no terminal
meu_time = input("Qual é o seu time?") #A função input() caputura algum dado informado pelo usuario
print("Seu time é: ", meu_time)
print("")
nome = "Ronaldo"
#Formas de saida da informação
#Primeira Forma
print('Primera forma: ', meu_time, nome)

#Segunda Forma
print(f"Segunda Forma: {meu_time} {nome}")

#Terceira forma
print("Terceira Forma: {} {}".format(meu_time, nome))

