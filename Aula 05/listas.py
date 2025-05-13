#Cria a lista
frutas = ["maça", "banana", "laranja","pera","abacaxi"]

print(frutas[2]) #Exibe um item da lista
print(frutas[-1]) #Le o ultimo
print(frutas[-2]) #Le o penultimo

print(20*"-")

#Cortar - Slice
print(frutas[0:2]) #Exibe os valores de indice 0 e 1 e corta o indice 2
print(frutas[1:3]) #Exibe os valores de indice 1 e 2 e corta o indice 3
print(frutas[:]) #Exibe todos os elementos
print(frutas[::2]) #Exibe elemtos pares

#Tamanho len()
print(len(frutas))

#Concatenar - Juntar (+)
mais_frutas = ["moango","uva"]
cesta_de_Frutas = frutas + mais_frutas
print(cesta_de_Frutas)

#Repetir o arrray(*)
repita = frutas * 2
print(repita)

#Adicionando elemtos
frutas.append("goiaba") #Adicona um elemento ao final da  lista
print(frutas)

frutas.insert(0, "melao") #Adiciona um elemento em uma posição especifica
print(frutas)

frutas_dois = ["tomate","kiwi"]
frutas.extend(frutas_dois) #Mais elementos a lista
print(frutas)
frutas.insert(2,frutas_dois)
print(frutas)

#Removendo dados da lista
frutas.remove("melao") #Remove o item
print(frutas)

elemento = frutas.pop(2)
print(frutas) #exibe o array sem o elemento retirado peleo pop
print(elemento) #Exibe somente o elemento 

