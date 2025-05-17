#Calcuadora
#Obs - Este código tem um erro na divisão
def calculadora(valor_um,valor_dois,operador):
    if operador == "+":
        resultado = valor_um + valor_dois
        return resultado
    elif operador == "-":
        resultado = valor_um - valor_dois
        return resultado
    elif operador == "*":
        resultado = valor_um * valor_dois
        return resultado
    elif operador == "/":
        resultado = valor_um / valor_dois
    else:
        resultado = "Operação inválida"
        return resultado
    

#Programação
numero_um = int(input("Informe o primeiro valor: "))
op = input("Informe a operação: (+,-,*,/)")
numero_dois = int(input("Informe o segundo Valor: "))

print(calculadora(numero_um,numero_dois,op))
