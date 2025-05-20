class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self): #Metodo para formatar string
        return f"Cliente: {self.nome} (CPF: {self.cpf})"