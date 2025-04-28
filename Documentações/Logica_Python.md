**Apostila: Variáveis e Estruturas de Decisão em Python**

---

### Introdução

Python é uma das linguagens de programação mais populares do mundo devido à sua simplicidade e facilidade de aprendizado. Nesta apostila, vamos explorar dois conceitos fundamentais para quem está iniciando: **variáveis**, **estruturas de decisão** e **estruturas de repetição**.

---

### Capítulo 1: Variáveis

#### O que são variáveis?
Variáveis são "caixinhas" onde guardamos informações. Em Python, nós não precisamos declarar o tipo da variável explicitamente; o Python detecta automaticamente.

#### Regras para criar variáveis
1. O nome deve começar com uma letra ou _ (underline).
2. Não pode conter espaços ou caracteres especiais.
3. O nome é sensível a maiúsculas e minúsculas.

#### Exemplos de uso
```python
# Criando variáveis
nome = "Maria"  # Texto (string)
idade = 25       # Número inteiro (int)
peso = 65.5      # Número decimal (float)
estudante = True  # Valor booleano (True ou False)

# Exibindo os valores
print("Nome:", nome)
print("Idade:", idade)
print("Peso:", peso)
print("É estudante?", estudante)
```

#### Exercício prático
1. Crie uma variável chamada `cidade` e atribua o nome da sua cidade.
2. Crie uma variável chamada `ano_nascimento` e atribua o ano em que você nasceu.
3. Exiba essas informações usando `print`.

---

### Capítulo 2: Estruturas de Decisão

#### O que são estruturas de decisão?
São formas de fazer com que o programa tome decisões baseadas em condições.

#### A estrutura `if`
O `if` avalia uma condição. Se for verdadeira, o código dentro do bloco será executado.

**Exemplo:**
```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
```

#### Estruturas `if...else`
O `else` é usado para definir o que acontece se a condição não for verdadeira.

**Exemplo:**
```python
idade = 16
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

#### Estruturas `if...elif...else`
Quando temos mais de uma condição, usamos `elif` (abreviação de "else if").

**Exemplo:**
```python
nota = 7
if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado.")
else:
    print("Reprovado.")
```

#### Operadores Relacionais
- `==` : igual a
- `!=` : diferente de
- `>`  : maior que
- `<`  : menor que
- `>=` : maior ou igual a
- `<=` : menor ou igual a

#### Operadores Lógicos
- `and` : e
- `or`  : ou
- `not` : não

**Exemplo com operadores:**
```python
idade = 20
estudante = True
if idade >= 18 and estudante:
    print("Você é um estudante maior de idade.")
```

#### Exercício prático
1. Peça ao usuário para digitar sua idade usando `input`.
2. Verifique se a idade é maior ou igual a 18.
3. Exiba "Você é maior de idade" ou "Você é menor de idade".

**Dica:** Use o código abaixo para receber entradas do usuário.
```python
idade = int(input("Digite sua idade: "))
```

---

### Capítulo 3: Estruturas de Repetição

#### O que são estruturas de repetição?
As estruturas de repetição permitem que um bloco de código seja executado diversas vezes com base em uma condição ou em uma sequência de valores.

#### Estrutura `for`
O `for` é usado para percorrer sequências, como listas ou intervalos de números.

**Exemplo:**
```python
for i in range(5):
    print("Número:", i)
```

#### Estrutura `while`
O `while` repete um bloco de código enquanto uma condição for verdadeira.

**Exemplo:**
```python
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

#### Comandos adicionais
- `break`: Encerra o laço antes do fim.
- `continue`: Pula para a próxima iteração do laço.

**Exemplo com `break` e `continue`:**
```python
for i in range(10):
    if i == 5:
        break  # Interrompe o laço quando i é 5
    if i % 2 == 0:
        continue  # Pula os números pares
    print("Número impar:", i)
```

#### Exercício prático
1. Use um `for` para imprimir os números de 1 a 10.
2. Use um `while` para somar os números de 1 a 100 e imprimir o resultado.

---

### Conclusão

Variáveis, estruturas de decisão e estruturas de repetição são conceitos essenciais para criar programas dinâmicos e interativos. Pratique os exemplos desta apostila e crie seus próprios códigos para reforçar o aprendizado. Em breve, você estará pronto para explorar estruturas mais avançadas!

---

