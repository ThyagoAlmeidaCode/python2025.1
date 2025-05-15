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
    print("----Escolha uma operação:---")
    print("\n1-Depositar \n2-Sacar \n3-Cosultar saldo \n4-Consultar histórico \n5-sair ")
    opcao = input("Escolha uma opção: ")

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
                    print("Deposito realizado con sucesso")
                    break
                else:
                    print("Valor invalido.")
            else: 
                print("Entrada invalida. Digite um numero.")
    elif opcao == "2":
        print("Sacar")
    elif opcao == "3":
        print("Saldo")
    elif opcao == "4":
        print("Historico")
    elif opcao == "5":
        print("Obrigado por usar nosso Banco.")
        break
    else: 
        print("Opção Invalida. Por favor, escolha uma opção do menu.")

    