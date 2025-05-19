# Tutorial Básico de Orientação a Objetos em Python para Iniciantes
Olá! Este tutorial foi criado para você, que está começando a dar os primeiros passos em Python e no mundo da programação orientada a objetos (OO). Vamos aprender juntos de forma simples e prática!

## O Que Você Vai Aprender:

A diferença entre programação procedural e orientada a objetos.
1. Os conceitos de classe, objeto, atributo e método.
2. Como criar suas próprias classes e objetos em Python.
3. Como usar o construtor (__init__) para configurar seus objetos.
4. Como interagir com os objetos, acessando seus atributos e chamando seus métodos.
5. Uma breve introdução aos conceitos de encapsulamento, herança e polimorfismo.

## Pré-requisitos:

1. Python instalado no seu computador.
2. Um editor de código de sua preferência (VS Code, PyCharm, Sublime Text, etc.).
3. Um pouco de familiaridade com a sintaxe básica do Python (variáveis, funções, etc.).


## Pensando em Objetos no Mundo Real
Antes de mergulharmos no código, vamos pensar um pouco sobre o mundo ao nosso redor. Quase tudo que vemos e interagimos pode ser considerado um objeto.

### Um carro tem características (cor, modelo, velocidade) e ações (acelerar, frear, buzinar).
### Uma pessoa tem características (nome, idade, altura) e ações (andar, falar, comer).
### Um livro tem características (título, autor, número de páginas) e pode ter ações (abrir, fechar, folhear).

Na programação orientada a objetos, a ideia é trazer essa forma de pensar para o nosso código. Em vez de apenas ter dados soltos e funções que os manipulam, nós agrupamos dados (características) e comportamentos (ações) dentro de objetos.

## Programação Procedural vs. Orientada a Objetos
Para entender melhor a OO, vamos comparar brevemente com a forma como talvez você já tenha programado: a programação procedural.

1. Na programação procedural, o foco principal está nas funções, que são blocos de código que realizam tarefas específicas. Os dados geralmente são separados das funções e podem ser manipulados por várias delas. Imagine uma receita de bolo: você tem os ingredientes (dados) e as instruções passo a passo (funções) para preparar o bolo.

2. Na programação orientada a objetos, o foco está nos objetos. Cada objeto combina dados (chamados de atributos) e funções que operam nesses dados (chamadas de métodos). Voltando ao exemplo do bolo, na OO, poderíamos pensar em um "Objeto Bolo" que tem atributos como sabor, tamanho e cobertura, e métodos como "assar", "decorar" e "comer".

A OO ajuda a organizar o código de uma maneira mais modular, reutilizável e fácil de entender, especialmente para projetos maiores e mais complexos.

## Os Quatro Pilares da Orientação a Objetos (Uma Introdução)
A orientação a objetos se baseia em alguns princípios fundamentais. Para começar, vamos conhecer quatro deles de forma bem básica:

1. Classe: É como um "molde" ou uma "planta" para criar objetos. Ela define quais atributos e métodos os objetos dessa classe terão. Pense na receita do bolo: a receita é a classe.
Objeto (ou Instância): É uma "cópia" concreta de uma classe. É o bolo pronto feito a partir da receita. Você pode ter vários bolos (objetos) feitos com a mesma receita (classe), cada um com suas próprias características (por exemplo, um com mais cobertura que o outro).
2. Atributo: São as características ou propriedades de um objeto. No nosso exemplo do bolo, o sabor, o tamanho e a cobertura seriam atributos. Na classe Cachorro, a raça, o nome e a idade seriam atributos.
3. Método: São as ações ou comportamentos que um objeto pode realizar. No bolo, "assar" e "decorar" seriam métodos. Na classe Cachorro, "latir" e "correr" seriam métodos.

## Mais tarde, vamos dar uma olhada em outros pilares importantes:

1. Encapsulamento: A ideia de "esconder" os detalhes internos de um objeto e fornecer uma maneira controlada de interagir com ele.
2. Herança: A capacidade de uma classe herdar características e comportamentos de outra classe, evitando a repetição de código.
3. Polimorfismo: A capacidade de objetos de diferentes classes responderem ao mesmo método de maneiras diferentes.
Mas não se preocupe com esses três agora! Vamos focar em classes, objetos, atributos e métodos para começar.

## Criando sua Primeira Classe em Python
Em Python, usamos a palavra-chave class para definir uma classe. Vamos criar uma classe simples chamada Cachorro:

```
class Cachorro:
    # Atributos (características) da classe
    raca = "Desconhecida"
    nome = ""
    idade = 0

    # Método (comportamento) da classe
    def latir(self):
        print("Au au!")
```

# Entendendo o Código:

*** Class Cachorro:: *** Aqui, estamos definindo uma nova classe chamada Cachorro. Por convenção, os nomes de classes em Python geralmente começam com letra maiúscula.
*** raca =  "Desconhecida", nome = "", idade = 0: *** Estas são variáveis de classe. Elas definem os atributos  que todo objeto da classe Cachorro terá por padrão.
*** def latir(self):: *** Esta é uma função dentro da classe, chamada método. Ela define um comportamento que os objetos Cachorro podem ter.
A palavra-chave *** self  ***é muito importante em Python. Ela é uma referência ao próprio objeto que está chamando o método. Todo método de instância (um método que opera em um objeto específico) precisa ter self como seu primeiro parâmetro.

## Criando Objetos (Instâncias) da Classe
Agora que temos a nossa classe Cachorro, podemos criar objetos (ou instâncias) dessa classe. É como usar o molde para fazer vários cachorros diferentes.



```
# Criando o primeiro objeto Cachorro
meu_cachorro = Cachorro()

# Criando o segundo objeto Cachorro
outro_cachorro = Cachorro()

```
Aqui, meu_cachorro e outro_cachorro são dois objetos distintos da classe Cachorro. Cada um deles terá os atributos e poderá executar os métodos definidos na classe.

## Acessando Atributos dos Objetos
Podemos acessar os atributos de um objeto usando a notação de ponto (.).


```
print(meu_cachorro.raca)  # Saída: Desconhecida
print(outro_cachorro.nome) # Saída:

# Podemos modificar os atributos de um objeto
meu_cachorro.nome = "Rex"
meu_cachorro.idade = 3
outro_cachorro.raca = "Poodle"
outro_cachorro.nome = "Lulu"

print(meu_cachorro.nome)  # Saída: Rex
print(meu_cachorro.idade) # Saída: 3
print(outro_cachorro.raca) # Saída: Poodle
```

Cada objeto tem seu próprio conjunto de valores para os atributos. Alterar o atributo de um objeto não afeta os outros objetos da mesma classe.

# Chamando Métodos dos Objetos
Da mesma forma, usamos a notação de ponto para chamar os métodos de um objeto.

```
meu_cachorro.latir()      # Saída: Au au!
outro_cachorro.latir()     # Saída: Au au!
```

Quando chamamos o método latir() em um objeto Cachorro, a função latir dentro da classe é executada para aquele objeto específico.

## O Método Construtor (__init__)
O método __init__ (com dois underscores antes e depois de "init") é um método especial em Python. Ele é chamado automaticamente quando um novo objeto é criado a partir de uma classe. Geralmente, usamos o __init__ para inicializar os atributos de um objeto com valores específicos no momento da sua criação.

Vamos modificar nossa classe Cachorro para usar o __init__:

```
class Cachorro:
    def __init__(self, raca, nome, idade):
        # Inicializando os atributos do objeto com os valores passados
        self.raca = raca
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"{self.nome} está latindo: Au au!")
```


## O que mudou:

Adicionamos o método __init__(self, raca, nome, idade). Ele recebe três parâmetros além de self: raca, nome e idade.
Dentro do __init__, usamos self.raca = raca, self.nome = nome e self.idade = idade para atribuir os valores passados como argumentos aos atributos do objeto que está sendo criado.
Agora, quando criamos um objeto Cachorro, precisamos passar os valores para esses atributos:


```
meu_cachorro = Cachorro("Golden Retriever", "Max", 2)
outro_cachorro = Cachorro("Poodle", "Lulu", 5)

print(meu_cachorro.nome)    # Saída: Max
meu_cachorro.latir()      # Saída: Max está latindo: Au au!
print(outro_cachorro.raca)   # Saída: Poodle
print(outro_cachorro.idade)  # Saída: 5
outro_cachorro.latir()     # Saída: Lulu está latindo: Au au!
```

O __init__ torna a criação de objetos mais flexível, pois podemos definir as características iniciais de cada objeto no momento em que ele é criado.

## Encapsulamento (Uma Breve Olhada)
O encapsulamento é a ideia de agrupar os atributos (dados) e os métodos (comportamentos) que operam nesses atributos dentro de uma classe. Ele também envolve controlar o acesso aos dados internos do objeto, protegendo-os de modificações diretas e inesperadas.

Em Python, o encapsulamento é geralmente feito por convenção. Usamos um underscore (_) no início do nome de um atributo para indicar que ele é "protegido" e não deve ser acessado diretamente fora da classe. Dois underscores (__) indicam um atributo "privado" (embora Python ainda permita um certo acesso).

Vamos ver um exemplo:

```
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial  # Usando um underscore para indicar proteção

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de {valor} realizado. Novo saldo: {self._saldo}")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self._saldo}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def verificar_saldo(self):
        print(f"Saldo atual: {self._saldo}")

minha_conta = ContaBancaria("Alice", 100)
minha_conta.depositar(50)
minha_conta.sacar(20)
minha_conta.verificar_saldo()
# print(minha_conta._saldo) # Evite acessar atributos "protegidos" diretamente
```

Aqui, _saldo é um atributo que consideramos "protegido". Idealmente, interagimos com o saldo através dos métodos depositar, sacar e verificar_saldo, que controlam como o saldo é modificado e acessado. Isso ajuda a manter a integridade dos dados da conta.

## Herança (Uma Introdução)
A herança permite que uma classe (chamada de classe filha ou subclasse) herde atributos e métodos de outra classe (chamada de classe pai ou superclasse). Isso promove a reutilização de código e a criação de hierarquias de classes.

Imagine que temos uma classe geral Animal com características comuns a todos os animais (como nome e um método emitir_som). Podemos criar classes mais específicas como Cachorro e Gato que herdam de Animal e adicionam seus próprios comportamentos específicos (latir e miar).

```
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico de animal")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

meu_animal = Animal("Desconhecido")
rex = Cachorro("Rex")
lulu = Gato("Lulu")

meu_animal.emitir_som() # Saída: Som genérico de animal
rex.emitir_som()      # Saída: Au au!
lulu.emitir_som()     # Saída: Miau!
```

Aqui, Cachorro e Gato herdam o atributo nome e o método emitir_som da classe Animal. Eles também podem sobrescrever métodos herdados para fornecer uma implementação mais específica, como vemos com o método emitir_som.

## Polimorfismo (Uma Introdução)
O polimorfismo (que significa "muitas formas") permite que objetos de diferentes classes respondam ao mesmo método de maneiras diferentes. Vimos um exemplo disso com a herança. Tanto o objeto Cachorro quanto o objeto Gato podem "emitir um som", mas a forma como eles fazem isso é diferente.

O polimorfismo torna o código mais flexível e extensível, pois podemos tratar objetos de diferentes classes de forma uniforme se eles compartilharem uma interface comum (por exemplo, um método com o mesmo nome).
