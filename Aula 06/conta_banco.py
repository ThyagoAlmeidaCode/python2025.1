#Solicita nome do titular
nome_titular = input("Informe o nome da conta do titular: ")

#Abetura da conta(Deposito inicial)
while True:
    deposito_inicial = input("Digite o valor de deposito inicial: ")
    if deposito_inicial.replace(".","",1).isdigit():
        deposito_inicial = float(deposito_inicial)
        if deposito_inicial >= 0:
            conta = (nome_titular, [deposito_inicial],[])
            
            break
        else:
            print("Valor Inválido! Digite um número")
    else:
        print("Valor Inválido! Digite um numero:")

#Operções (Depositar, Sacar, Consultar saldo, Consultar historico, sair)

while True:     
    print("\n----Escolha uma operação:---")
    print("\n1-Depositar \n2-Sacar \n3-Cosultar saldo \n4-Consultar histórico \n5-sair ")
    opcao = input("Escolha uma opção:\n ")

    if opcao == "1":
        while True:
            valor_deposito = input("Digite um valor de deposito: ")
            if valor_deposito.replace(".","",1).isdigit():
                valor_deposito = float(valor_deposito)
                if valor_deposito >= 0:
                    #valor_deposito += conta[1][0]
                    #Soma o valor do saldo
                    conta[1][0] += valor_deposito
                    #Adicona ao historico
                    conta[2].append("Depósito de R$: {} ".format(valor_deposito))
                    print("\nDeposito realizado con sucesso")
                    break
                else:
                    print("\nValor invalido.")
            else: 
                print("\nEntrada invalida. Digite um numero.")
    elif opcao == "2":
        while True:
            valor_saque= input("Digite o valor a sacar: ")
            if valor_saque.replace('.', '', 1).isdigit():
                valor_saque = float(valor_saque)
                if valor_saque > 0:
                    if conta[1][0] >= valor_saque:
                        # Atualiza o saldo
                        conta[1][0] -= valor_saque
                        # Adiciona ao histórico
                        conta[2].append(f"Saque de: R$ {valor_saque:.2f}")
                        print("\nSaque realizado com sucesso.")
                        break
                    else:
                        print("\nSaldo insuficiente.")
                else:
                    print("\nValor de saque inválido.")
            else:
                print("\nEntrada inválida. Digite um número.")
    elif opcao == "3":
        # Consulta o saldo (primeiro elemento da lista no índice 1 da tupla)
        print(f"\nSaldo atual: R$ {conta[1][0]:.2f}")
    elif opcao == "4":
        # Consulta o histórico (lista no índice 2 da tupla)
        if conta[2]:
            print("\nHistórico de Transações:")
            for transacao in conta[2]:
                print(f"- {transacao}")
        else:
            print("\nNenhuma transação realizada ainda.")
    elif opcao == "5":
        print(f"\n Sr(a) {conta[0]} Obrigado por usar nosso Banco.")
        break
    else: 
        print("\nOpção Invalida. Por favor, escolha uma opção do menu.")

    

    """ 
    Para que serve .2f?

    Basicamente, .2f dentro de uma string formatada (usando f-strings ou o operador %) serve para dizer ao Python para formatar um número float da seguinte maneira:

    .2: Indica que você quer exibir o número com duas casas decimais após o ponto. Isso é muito comum para representar valores de dinheiro (centavos).

    f: Especifica que o número a ser formatado é um ponto flutuante (um número com casas decimais). 
    """