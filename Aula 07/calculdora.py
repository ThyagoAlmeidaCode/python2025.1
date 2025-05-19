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
        if valor_dois == 0:
            print("Não é possivel divisão por zero.")
        else:
            resultado = valor_um / valor_dois
            #Faltou o ruturn do resultado
            return resultado
    else:
        resultado = "Operação inválida"
        return resultado
    

#Programação
numero_um = int(input("Informe o primeiro valor: "))
op = input("Informe a operação: (+,-,*,/)")
numero_dois = int(input("Informe o segundo Valor: "))

print(calculadora(numero_um,numero_dois,op))
