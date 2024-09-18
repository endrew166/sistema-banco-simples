texto = f""" 
    Menu do Banco
    [1] - Depositar:
    [2] - Sacar:
    [3] - Verificar extrato:
    [0] - Sair

"""
saldo = 0
extrato = []
extrato02 = []
valor_saque = 0

while True:
    opcao = input(texto)

    if opcao == "1":
        valor = float(input("Valor a ser depositado: R$ "))

        if valor <= 0:
            print("O valor do depósito deve ser maior que zero.")
        else:
            saldo += valor  # incrementar o saldo
            extrato.append(saldo)  # Adicionando o novo saldo a lista
            print(f"Depósito realizado com sucesso")

    elif opcao == "2":

        print("Saque")

        valor_saque = float(input("Valor que deseja sacar: "))

        # verificar todos os critérios do desafio

        if valor_saque <= 500 and saldo >= valor_saque and len(extrato02) < 3:

            saldo -= valor_saque

            extrato02.append(valor_saque)

            print("Saque feito com sucesso.")

        else:
            # Mensagens de erro

            if valor_saque > 500:
                print("O valor máximo para saque é R$ 500.")

            if saldo < valor_saque:
                print("Saldo insuficiente.")

            if len(extrato02) >= 3:
                print("Limite de saques diários atingido.")

    elif opcao == "3":

        print("Extrato:")

        if extrato:  # caso existir item na lista

            for i in extrato:  # exibir todos os itens da lista

                if i > 0:
                    print(f"Valor depositado: R$ {i:.2f}")


        if extrato02:  # caso existir item na lista
            for i in extrato02:  # exibir todos os itens da lista

                if i > 0:
                    print(f"Valor retirado: R$ {i:.2f}")

        if not extrato and not extrato02: #confirando se a lista está vaiza ou não

            print("Nenhuma transação registrada.")

        print(f"Saldo final: R$ {saldo:.2f}")  # mostrar resultado final do saldo

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")