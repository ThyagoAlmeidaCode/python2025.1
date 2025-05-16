# O que é uma função?
Uma função é um bloco de código reutilizável que executa uma tarefa específica.

## Por que usar funções?
1. Para organizar melhor o código
2. Para reaproveitar código em várias partes do programa
3. Para deixar o programa mais legível e modular

## Como criar uma função
Usamos a palavra-chave def para definir uma função.

Sintaxe básica
```
def nome_da_funcao():
    # bloco de código
    print("Olá, mundo!")
```

## Exemplo prático

```
def saudacao():
    print("Bem-vindo ao mundo da programação em Python!")

# Chamando a função
saudacao()
```


## Funções com parâmetros
Podemos passar informações para a função através de parâmetros.
### Exemplo:

```
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Thyago")
saudacao("Maria")
```
## Funções com retorno de valores
Usamos return para retornar um valor da função.

### Exemplo:
```
def soma(a, b):
    return a + b

resultado = soma(10, 5)
print("Resultado da soma:", resultado)
```

## Funções com múltiplos parâmetros
Podemos passar vários parâmetros para uma função:

```
def apresentar_pessoa(nome, idade, cidade):
    print(f"{nome} tem {idade} anos e mora em {cidade}.")

apresentar_pessoa("João", 25, "Niterói")
```

## Parâmetros com valor padrão
É possível definir valores padrão para parâmetros, que serão usados se o valor não for passado.

```
def saudacao(nome="visitante"):
    print(f"Olá, {nome}!")

saudacao("Thyago")
saudacao()  # usa o valor padrão
```

## Funções que retornam múltiplos valores
Você pode retornar vários valores separados por vírgula:

```
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao

s, sub = operacoes(10, 5)
print("Soma:", s)
print("Subtração:", sub)
```
## Funções como ferramentas reutilizáveis
Podemos usar funções para resolver problemas mais elaborados de forma organizada.

### Exemplo: Verificar se um número é par
```
def eh_par(numero):
    return numero % 2 == 0

print(eh_par(4))  # True
print(eh_par(7))  # False
```
## Função main() (boa prática)
Em programas maiores, criamos uma função main() para organizar a execução:

```
def saudacao(nome):
    print(f"Olá, {nome}!")

def main():
    nome = input("Digite seu nome: ")
    saudacao(nome)

# Só executa se o arquivo for rodado diretamente
if __name__ == "__main__":
    main()
```

## Desafios para praticar
1. Crie uma função que receba uma lista de números e retorne a média.
2. Crie uma função que receba um número e diga se ele é primo.
3. Crie uma função que simule um saque em um caixa eletrônico (com valor de saque e saldo atual).

## Conclusão
As funções são essenciais para escrever códigos organizados, reutilizáveis e fáceis de manter. Agora que você entendeu como elas funcionam, experimente criar suas próprias funções para resolver pequenos problemas do dia a dia.