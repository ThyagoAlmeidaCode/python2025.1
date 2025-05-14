# Listas em Python: Flexibilidade em Suas Mãos
Imagine uma lista de compras. Você pode adicionar itens, remover, alterar a ordem, certo? As listas em Python funcionam de maneira bem parecida!

## O que são listas?

Listas são sequências ordenadas de itens. Esses itens podem ser de diferentes tipos (números, textos, outras listas, etc.). A grande característica das listas é que elas são mutáveis, ou seja, podemos modificar seu conteúdo depois de criadas.

## Como criar uma lista?

Usamos colchetes [] para definir uma lista e separamos os itens por vírgula.

```
# Uma lista de frutas
frutas = ["maçã", "banana", "laranja"]
print(frutas)  # Saída: ['maçã', 'banana', 'laranja']

# Uma lista de números
numeros = [1, 5, 10, 2]
print(numeros)  # Saída: [1, 5, 10, 2]

# Uma lista com diferentes tipos de dados
misturado = ["olá", 3.14, True]
print(misturado)  # Saída: ['olá', 3.14, True]

# Uma lista vazia
lista_vazia = []
print(lista_vazia)  # Saída: []

```
## Acessando itens da lista (Indexação)

Cada item em uma lista tem uma posição, chamada de índice. O índice sempre começa em 0 para o primeiro item, 1 para o segundo, e assim por diante.

```
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
```

## Modificando itens da lista

Como as listas são mutáveis, podemos alterar seus elementos diretamente pelo índice.

```
frutas = ["maçã", "banana", "laranja"]

# Alterando o item no índice 1
frutas[1] = "morango"
print(frutas)  # Saída: ['maçã', 'morango', 'laranja']
```

## Adicionando itens à lista

Existem algumas maneiras de adicionar itens a uma lista:

1. append(): Adiciona um item ao final da lista.
2. insert(índice, item): Insere um item em uma posição específica.
<!-- end list -->

```
frutas = ["maçã", "banana"]

# Adicionando "uva" ao final da lista
frutas.append("uva")
print(frutas)  # Saída: ['maçã', 'banana', 'uva']

# Inserindo "manga" na posição de índice 1
frutas.insert(1, "manga")
print(frutas)  # Saída: ['maçã', 'manga', 'banana', 'uva']
```

## Removendo itens da lista

Também temos diferentes formas de remover itens:

1. remove(item): Remove a primeira ocorrência do item especificado.
2. pop(índice): Remove o item no índice especificado e o retorna. Se nenhum índice for especificado, remove e retorna o último item.
3. del lista[índice]: Remove o item no índice especificado (não retorna o valor).
<!-- end list -->

```
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
```

## Outras operações úteis com listas

1. len(lista): Retorna o número de itens na lista.
2. lista1 + lista2: Concatena duas listas.
3. item in lista: Verifica se um item existe na lista (retorna True ou False).
4. lista.sort(): Ordena a lista (modifica a lista original).
5. sorted(lista): Retorna uma nova lista ordenada (não modifica a original).
<!-- end list -->

```
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
```

# Tuplas em Python: Imutabilidade é a Palavra-Chave
Pense em algo que você não pode mudar depois de criado, como as coordenadas de um ponto fixo. As tuplas em Python se comportam de maneira similar.

## O que são tuplas?

Tuplas são sequências ordenadas de itens, assim como as listas. A principal diferença é que as tuplas são imutáveis, o que significa que, uma vez criadas, você não pode alterar, adicionar ou remover seus elementos.

## Como criar uma tupla?

Usamos parênteses () para definir uma tupla e separamos os itens por vírgula. Embora os parênteses sejam opcionais em alguns casos, é uma boa prática usá-los para clareza.



```
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
```

A forma de acessar os itens de uma tupla é a mesma das listas, utilizando os índices.

```
cores = ("vermelho", "azul", "verde")

primeira_cor = cores[0]
print(primeira_cor)  # Saída: vermelho

ultima_cor = cores[-1]
print(ultima_cor)  # Saída: verde
```

## Imutabilidade das tuplas

Aqui está o ponto crucial: você não pode modificar uma tupla depois de criada. Qualquer tentativa de alterar um elemento resultará em um erro.


```
cores = ("vermelho", "azul", "verde")

# A linha abaixo causará um erro!
# cores[1] = "amarelo"

# A linha abaixo também causará um erro!
# cores.append("branco")
```

# Operações com tuplas

Apesar de não poderem ser modificadas, podemos realizar algumas operações com tuplas:

1. len(tupla): Retorna o número de itens na tupla.
2. tupla1 + tupla2: Concatena duas tuplas, criando uma nova tupla.
3. item in tupla: Verifica se um item existe na tupla.
<!-- end list -->

```
numeros_tupla = (1, 2, 3, 1)

print(len(numeros_tupla))  # Saída: 4

outra_tupla = (4, 5)
tupla_completa = numeros_tupla + outra_tupla
print(tupla_completa)  # Saída: (1, 2, 3, 1, 4, 5)

print(2 in numeros_tupla)  # Saída: True
print(6 in numeros_tupla)  # Saída: False
```

## Quando usar listas e quando usar tuplas?
1. Listas: Use quando você precisar de uma coleção de itens que podem ser modificados, como adicionar, remover ou alterar elementos. São ideais para representar listas de compras, coleções de dados que podem mudar, etc.

2. Tuplas: Use quando você precisar de uma coleção de itens que não devem ser alterados após a criação. São úteis para representar dados fixos, como coordenadas, dias da semana, meses do ano, ou quando você quer garantir que os dados não sejam acidentalmente modificados. As tuplas também podem ser um pouco mais eficientes em termos de memória e desempenho em algumas situações.

# Curiosidade
## Podemos alterar uma lista dentro de uma tupla?

A resposta é: Sim, você pode modificar uma lista que está dentro de uma tupla.

A imutabilidade da tupla se aplica aos elementos que ela armazena. Uma vez que a tupla é criada, você não pode adicionar, remover ou substituir esses elementos por outros objetos. No entanto, se um desses elementos for um objeto mutável, como uma lista, você pode modificar o conteúdo desse objeto mutável.

Vamos ver um exemplo para deixar isso mais claro:

```
minha_tupla = ("texto", [1, 2, 3], True)

print(minha_tupla)  # Saída: ('texto', [1, 2, 3], True)

# Tentando substituir a lista por outro objeto (isso não é permitido!)
# minha_tupla[1] = [4, 5, 6]  # Isso geraria um erro: TypeError: 'tuple' object does not support item assignment

# Mas podemos modificar o conteúdo da lista que está dentro da tupla
minha_tupla[1].append(4)
minha_tupla[1].remove(1)

print(minha_tupla)  # Saída: ('texto', [2, 3, 4], True)
```

No exemplo acima:

1. Criamos uma tupla chamada minha_tupla que contém uma string, uma lista e um booleano.
2. Tentamos substituir a lista inteira por outra lista, o que resultou em um erro porque as tuplas não suportam a atribuição de novos itens em índices existentes.
3. No entanto, acessamos a lista que está no índice 1 da tupla (minha_tupla[1]) e usamos os métodos append() e remove() para modificar o conteúdo dessa lista. Isso é permitido porque estamos modificando um objeto mutável (a lista) que está dentro da tupla, e não tentando alterar a tupla em si.
Em resumo:

A tupla em si não pode ser alterada (você não pode mudar os objetos que ela contém). Mas se um dos objetos dentro da tupla for mutável (como uma lista, um dicionário ou um conjunto), você pode modificar esse objeto internamente.