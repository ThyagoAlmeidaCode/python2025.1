# Solicita o nome do titular da conta e armazena na variável nome_titular
nome_titular = input("Informe o nome da conta do titular: ")

# Bloco para abertura da conta, solicitando o depósito inicial
while True:
    # Solicita o valor do depósito inicial
    deposito_inicial = input("Digite o valor de deposito inicial: ")
    # Verifica se a entrada é um número (permite um ponto como separador decimal)
    if deposito_inicial.replace(".", "", 1).isdigit():
        # Converte a entrada para um número de ponto flutuante
        deposito_inicial = float(deposito_inicial)
        # Verifica se o depósito inicial é um valor não negativo
        if deposito_inicial >= 0:
            # Cria uma tupla representando a conta: (nome do titular, [saldo], [histórico de transações])
            conta = (nome_titular, [deposito_inicial], [])
            # Sai do loop de abertura da conta
            break
        else:
            # Exibe mensagem de erro se o valor digitado for negativo
            print("Valor Inválido! Digite um número positivo.")
    else:
        # Exibe mensagem de erro se a entrada não for um número
        print("Valor Inválido! Digite um numero:")

# Bloco para as operações bancárias (depositar, sacar, consultar saldo, consultar histórico, sair)
while True:
    # Exibe o menu de opções para o usuário
    print("\n----Escolha uma operação:---")
    print("\n1-Depositar \n2-Sacar \n3-Cosultar saldo \n4-Consultar histórico \n5-sair ")
    # Solicita a escolha da operação ao usuário
    opcao = input("Escolha uma opção:\n ")

    # Se a opção escolhida for "1" (Depositar)
    if opcao == "1":
        # Loop para solicitar o valor do depósito até que uma entrada válida seja fornecida
        while True:
            # Solicita o valor a ser depositado
            valor_deposito = input("Digite um valor de deposito: ")
            # Verifica se a entrada é um número (permite um ponto como separador decimal)
            if valor_deposito.replace(".", "", 1).isdigit():
                # Converte a entrada para um número de ponto flutuante
                valor_deposito = float(valor_deposito)
                # Verifica se o valor do depósito é não negativo
                if valor_deposito >= 0:
                    # Adiciona o valor do depósito ao saldo da conta (o saldo está na primeira posição da lista no índice 1 da tupla 'conta')
                    conta[1][0] += valor_deposito
                    # Adiciona uma mensagem ao histórico de transações (a lista de histórico está no índice 2 da tupla 'conta')
                    conta[2].append(f"Depósito de R$: {valor_deposito:.2f}")
                    # Informa ao usuário que o depósito foi realizado com sucesso
                    print("\nDeposito realizado con sucesso")
                    # Sai do loop de depósito
                    break
                else:
                    # Exibe mensagem de erro se o valor do depósito for inválido
                    print("\nValor invalido.")
            else:
                # Exibe mensagem de erro se a entrada não for um número
                print("\nEntrada invalida. Digite um numero.")
    # Se a opção escolhida for "2" (Sacar)
    elif opcao == "2":
        # Loop para solicitar o valor do saque até que uma entrada válida seja fornecida
        while True:
            # Solicita o valor a ser sacado
            valor_saque = input("Digite o valor a sacar: ")
            # Verifica se a entrada é um número (permite um ponto como separador decimal)
            if valor_saque.replace('.', '', 1).isdigit():
                # Converte a entrada para um número de ponto flutuante
                valor_saque = float(valor_saque)
                # Verifica se o valor do saque é positivo
                if valor_saque > 0:
                    # Verifica se o saldo da conta é suficiente para o saque
                    if conta[1][0] >= valor_saque:
                        # Subtrai o valor do saque do saldo da conta
                        conta[1][0] -= valor_saque
                        # Adiciona uma mensagem ao histórico de transações
                        conta[2].append(f"Saque de: R$ {valor_saque:.2f}")
                        # Informa ao usuário que o saque foi realizado com sucesso
                        print("\nSaque realizado com sucesso.")
                        # Sai do loop de saque
                        break
                    else:
                        # Informa ao usuário que o saldo é insuficiente
                        print("\nSaldo insuficiente.")
                else:
                    # Exibe mensagem de erro se o valor do saque for inválido
                    print("\nValor de saque inválido.")
            else:
                # Exibe mensagem de erro se a entrada não for um número
                print("\nEntrada inválida. Digite um número.")
    # Se a opção escolhida for "3" (Consultar saldo)
    elif opcao == "3":
        # Exibe o saldo atual da conta (formatado com duas casas decimais)
        print(f"\nSaldo atual: R$ {conta[1][0]:.2f}")
    # Se a opção escolhida for "4" (Consultar histórico)
    elif opcao == "4":
        # Verifica se há alguma transação no histórico
        if conta[2]:
            # Exibe o cabeçalho do histórico de transações
            print("\nHistórico de Transações:")
            # Itera sobre cada transação no histórico e a imprime
            for transacao in conta[2]:
                print(f"- {transacao}")
        else:
            # Informa ao usuário que ainda não foram realizadas transações
            print("\nNenhuma transação realizada ainda.")
    # Se a opção escolhida for "5" (Sair)
    elif opcao == "5":
        # Exibe uma mensagem de agradecimento e o nome do titular
        print(f"\n Sr(a) {conta[0]} Obrigado por usar nosso Banco.")
        # Sai do loop principal de operações
        break
    # Se a opção escolhida não for nenhuma das válidas
    else:
        # Informa ao usuário que a opção é inválida
        print("\nOpção Invalida. Por favor, escolha uma opção do menu.")