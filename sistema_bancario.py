print("-+"*20)
print("Caixa Eletrônico")
print("-+"*20)

print("Escolha a operação desejada!")
menu = "[D] DEPOSITO | [S] SAQUE | [E] EXTRATO | [Q] SAIR |\n ==> "



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do Deposito: R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha! Valor inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    
    elif opcao == "q": 
        print("Sistema Finalizado!")
        break
    
    else:
        print("Operação inválida, Tente Novamente!.")