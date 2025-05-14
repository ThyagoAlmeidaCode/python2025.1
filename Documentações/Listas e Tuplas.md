frutas = ["maçã", "banana", "laranja"]

# Acessando o primeiro item (índice 0)
primeira_fruta = frutas[0]
print(primeira_fruta)  # Saída: maçã

# Acessando o segundo item (índice 1)
segunda_fruta = frutas[1]
print(segunda_fruta)  # Saída: banana

# Acessando o último item usando índice negativo (-1)
ultima_fruta = frutas[-1]
print(ultima_fruta)  # Saída: laranja
Modificando itens da lista

Como as listas são mutáveis, podemos alterar seus elementos diretamente pelo índice.

Python

frutas = ["maçã", "banana", "laranja"]

# Alterando o item no índice 1
frutas[1] = "morango"
print(frutas)  # Saída: ['maçã', 'morango', 'laranja']
Adicionando itens à lista

Existem algumas maneiras de adicionar itens a uma lista:

append(): Adiciona um item ao final da lista.
insert(índice, item): Insere um item em uma posição específica.
<!-- end list -->

Python

frutas = ["maçã", "banana"]

# Adicionando "uva" ao final da lista
frutas.append("uva")
print(frutas)  # Saída: ['maçã', 'banana', 'uva']

# Inserindo "manga" na posição de índice 1
frutas.insert(1, "manga")
print(frutas)  # Saída: ['maçã', 'manga', 'banana', 'uva']
Removendo itens da lista

Também temos diferentes formas de remover itens:

remove(item): Remove a primeira ocorrência do item especificado.
pop(índice): Remove o item no índice especificado e o retorna. Se nenhum índice for especificado, remove e retorna o último item.
del lista[índice]: Remove o item no índice especificado (não retorna o valor).
<!-- end list -->

Python

frutas = ["maçã", "banana", "laranja", "banana"]

# Removendo a primeira ocorrência de "banana"
frutas.remove("banana")
print(frutas)  # Saída: ['maçã', 'laranja', 'banana']

# Removendo o item no índice 1 ("laranja") e guardando-o
fruta_removida = frutas.pop(1)
print(frutas)  # Saída: ['maçã', 'banana']
print(f"A fruta removida foi: {fruta_removida}")  # Saída: A fruta removida foi: laranja

# Removendo o item no índice 0 ("maçã")
del frutas[0]
print(frutas)  # Saída: ['banana']
Outras operações úteis com listas

len(lista): Retorna o número de itens na lista.
lista1 + lista2: Concatena duas listas.
item in lista: Verifica se um item existe na lista (retorna True ou False).
lista.sort(): Ordena a lista (modifica a lista original).
sorted(lista): Retorna uma nova lista ordenada (não modifica a original).
<!-- end list -->

Python

numeros = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numeros))  # Saída: 8

outros_numeros = [10, 20]
todos_numeros = numeros + outros_numeros
print(todos_numeros)  # Saída: [3, 1, 4, 1, 5, 9, 2, 6, 10, 20]

print(5 in numeros)  # Saída: True
print(15 in numeros) # Saída: False

numeros.sort()
print(numeros)  # Saída: [1, 1, 2, 3, 4, 5, 6, 9]

numeros_ordenados = sorted([7, 0, 8])
print(numeros_ordenados)  # Saída: [0, 7, 8]
Tuplas em Python: Imutabilidade é a Palavra-Chave
Pense em algo que você não pode mudar depois de criado, como as coordenadas de um ponto fixo. As tuplas em Python se comportam de maneira similar.

O que são tuplas?

Tuplas são sequências ordenadas de itens, assim como as listas. A principal diferença é que as tuplas são imutáveis, o que significa que, uma vez criadas, você não pode alterar, adicionar ou remover seus elementos.

Como criar uma tupla?

Usamos parênteses () para definir uma tupla e separamos os itens por vírgula. Embora os parênteses sejam opcionais em alguns casos, é uma boa prática usá-los para clareza.

Python

# Uma tupla de cores
cores = ("vermelho", "azul", "verde")
print(cores)  # Saída: ('vermelho', 'azul', 'verde')

# Uma tupla de números
valores = (10, 20, 30)
print(valores)  # Saída: (10, 20, 30)

# Uma tupla com um único elemento (note a vírgula!)
unica = ("elemento",)
print(unica)  # Saída: ('elemento',)

# Uma tupla vazia
tupla_vazia = ()
print(tupla_vazia)  # Saída: ()

# Criando uma tupla sem parênteses (menos recomendado)
pontos = 1, 5
print(pontos)  # Saída: (1, 5)
Acessando itens da tupla (Indexação)

A forma de acessar os itens de uma tupla é a mesma das listas, utilizando os índices.

Python

cores = ("vermelho", "azul", "verde")

primeira_cor = cores[0]
print(primeira_cor)  # Saída: vermelho

ultima_cor = cores[-1]
print(ultima_cor)  # Saída: verde
Imutabilidade das tuplas

Aqui está o ponto crucial: você não pode modificar uma tupla depois de criada. Qualquer tentativa de alterar um elemento resultará em um erro.

Python

cores = ("vermelho", "azul", "verde")

# A linha abaixo causará um erro!
# cores[1] = "amarelo"

# A linha abaixo também causará um erro!
# cores.append("branco")
Operações com tuplas

Apesar de não poderem ser modificadas, podemos realizar algumas operações com tuplas:

len(tupla): Retorna o número de itens na tupla.
tupla1 + tupla2: Concatena duas tuplas, criando uma nova tupla.
item in tupla: Verifica se um item existe na tupla.
<!-- end list -->

Python

numeros_tupla = (1, 2, 3, 1)

print(len(numeros_tupla))  # Saída: 4

outra_tupla = (4, 5)
tupla_completa = numeros_tupla + outra_tupla
print(tupla_completa)  # Saída: (1, 2, 3, 1, 4, 5)

print(2 in numeros_tupla)  # Saída: True
print(6 in numeros_tupla)  # Saída: False
Quando usar listas e quando usar tuplas?
Listas: Use quando você precisar de uma coleção de itens que podem ser modificados, como adicionar, remover ou alterar elementos. São ideais para representar listas de compras, coleções de dados que podem mudar, etc.

Tuplas: Use quando você precisar de uma coleção de itens que não devem ser alterados após a criação. São úteis para representar dados fixos, como coordenadas, dias da semana, meses do ano, ou quando você quer garantir que os dados não sejam acidentalmente modificados. As tuplas também podem ser um pouco mais eficientes em termos de memória e desempenho em algumas situações.