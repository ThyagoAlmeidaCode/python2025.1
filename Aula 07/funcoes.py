""" 
    O que é funções?
        -> As funções são bloco de código que realizam uma tarefa.
        -> Esses códigos são reutilizaveis
        -> Ajudam a organizar o código
        -> Ajuda a não repetir códigos desnecessariamente
"""

#Sintaxe (Escrita) da função:
def nome_funcao():
    """
    #Corpo da função
    #Comandos da função 
    """
    
print("Função Simples")
def saudacao():
    print("Ola! Boa noite Ass: Bonner")

#Precisamos chamar a função
saudacao()

print(20*"-")
print("Função com parametros")

def saudacao_turma(nome_turma):
    print(f"Boa noite! {nome_turma} ")
    print("Essa é uma função")

saudacao_turma("2025.1 Top")
saudacao_turma("Galera")

print(20*"-")
print("Função com retorno")

def soma():
    return 1 + 2

print("O resultado é: ",  soma())