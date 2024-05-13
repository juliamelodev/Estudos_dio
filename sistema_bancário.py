menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True: #Utilizamos quando determinada condição for satiisfeita.

    opcao = input(menu) #Voce vai escolher uma opção do menu e essa aopção será armazenada na variável 'opcao'

    if opcao == "d": # if the option is
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0: #evitar depósito com valores negativos
            saldo += valor #se o valor insirido pelo usuário for válido 
            extrato += f"Depósito: R${valor:.2f}\n" #verificação
        else: #caso o valor seja negativo e caso não for do jeito desejado.
            print("Operação falhou! O valor informado é inválido.") #se não for como a verificação desejada
    elif opcao == "s":
        valor = float(input("Informe o valor do sacar: "))
        # 3 verificações do saque. 1-
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUE

         #what we give back to the user
        if excedeu_saldo:
            print("Operação falhou! Seu saldo é insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação falhou! Limite máximo de saques atingido. Por favor, tente novamente mmais tarde.")
        #If you are within the withdrawal rules:
        elif valor > 0: #Posiive value
            saldo -= valor # withdrawing the value form the account
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "e":
        print("\n============== EXTRATO ===============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
    
    elif opcao == "q":
        break 

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

        
  