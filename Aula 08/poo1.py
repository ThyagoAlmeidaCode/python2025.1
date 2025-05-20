#Criando o nosso primeiro modelo (Classe)
class Cachorro:
    #Atributos (Variaveis metidas)
    raca = ""
    nome = ""
    idade = 0
    #Métodos (Funções metidas)
    def latir(self):
        print("Au Au!")

##Usa o modelo (Intancia)
cachorro_um = Cachorro()
cachorro_um.raca = "Viaralata"
cachorro_um.nome = "Xuxu"
print(f"A raça do meu cachorro é: {cachorro_um.raca} ")
cachorro_um.latir()

cachorro_dois = Cachorro()
cachorro_dois.raca = "Poodle"
cachorro_dois.nome = "Python"
cachorro_dois.latir()
print(f"O nome do cachorro dois é: {cachorro_dois.nome} ")