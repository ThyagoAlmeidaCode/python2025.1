""" Desafio: 
Remover Duplicatas: Dada a lista elementos = [5, 2, 5, 8, 1, 8, 3], crie uma nova lista contendo apenas os elementos únicos da lista original, mantendo a ordem original de aparição, e imprima a nova lista. 
"""
elementos = [5, 2, 5, 8, 1, 8, 3] #Aqui, definimos a lista original com os elementos duplicados.
unicos = []#Criamos uma lista vazia chamada

for i in elementos: #Percorre os elentos da lista
    if i not in unicos: #Para cada i verifica se ja contem no array unicos
        unicos.append(i) #Adciona itens ao array 
print(unicos) #Exibe o novo array