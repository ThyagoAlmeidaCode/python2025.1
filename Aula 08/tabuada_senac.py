#From informa de qual arquivo a gente vai importar
#Import eu import a classe de dentro do arquivo
from class_tabuada import Tabuada

#Instanciar a classe

valor = int(input("Informe o valor da tabuada: "))

tab_um = Tabuada(valor)
tab_um.soma()

print(20*"-")
tab_um.subtracao()

print(20*"-")
tab_um.multiplicacao()

print(20*"-")
tab_um.divisao()

