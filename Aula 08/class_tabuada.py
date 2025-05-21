class Tabuada:
    #Metodo construtor
    def __init__(self,numero):
        self.valor = numero
        self._resultado = 0

    #Metodo soma
    def soma(self):
        for i in range(1,11):
            self._resultado = self.valor + i
            print("{} + {} = {}".format(self.valor,i,self._resultado))
    
    #Metodo subtração
    def subtracao(self):
        for i in range(1,11):
            self._resultado = self.valor - i
            print("{} - {} = {}".format(self.valor,i,self._resultado))
    
    #Metodo Multiplicação
    def multiplicacao(self):
        for i in range(1,11):
            self._resultado = self.valor * i
            print("{} * {} = {}".format(self.valor,i,self._resultado))
    
    #Metodo Divisão
    def divisao(self):
        for i in range(1,11):
            self._resultado = self.valor / i
            print("{} / {} = {}".format(self.valor,i,self._resultado))