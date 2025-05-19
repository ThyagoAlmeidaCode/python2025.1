#Criando o nosso primeiro modelo (Classe)
class Cachorro:    
    #Metodo construtor
    def __init__(self,raca_cao,nome_cao,idade_cao):
        self.raca = raca_cao
        self.nome = nome_cao
        self.idade = idade_cao       

    #Métodos (Funções metidas)
    def latir(self):
        print("Au Au!")

##Usa o modelo (Intancia)
cachorro_um = Cachorro("Golden","MadMax",10)
cachorro_um.latir()
print(f"A raça do meu cachorro é: {cachorro_um.raca} ")

cachorro_dois = Cachorro("Poodle","FIFI",15)
cachorro_dois.latir()
print(f"O nome do cachorro dois é: {cachorro_dois.nome} ")