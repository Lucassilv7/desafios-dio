deposito = 0
tent = 0
saque = 0
lim_saque = 1
saldo = 400

nome = input("Insira seu nome: ")
operacao = int(input(f"Prazer {nome}! Seja bem vindo ao Banco R, "
                     f"qual opereção deseja realizar hoje:\n [1] - Depósito\n [2] - Saque\n "
                     f"[3] - Extrato\n"))

if operacao == 1:
    quant = float(input("Insira a quantia do depósito e depois confirme seu nome:\n "))
    key = str(input(" "))
    while tent <= 2:
        if key == nome:
            deposito = quant
            print("Depósito realizado com sucesso!")
            break
        else:
            print("Nome de confirmação errado\n")
            if tent == 1:
                print("Você tem mais uma tentativa, caso erre sua conta será bloqueada")
            elif tent == 2:
                print("Sua conta foi bloqueada por várias tentativas erradas")
                break
            key = str(input(" "))
            tent += 1
elif operacao == 2:
    quant = float(input("Informe a quantia para saque e depois confime seu nome:\n"))
    if quant > 500.00:
        print("O limite máximo de saque para esta conta é de R$500,00")
        exit()
    if saldo >= quant:
        while lim_saque <= 3:
            key = str(input(" "))
            while tent <= 2:
                if key == nome:
                    saque = quant
                    print("Saque realizado com sucesso!")
                    break
                else:
                    print("Nome de confirmação errado\n")
                    if tent == 1:
                        print("Você tem mais uma tentativa, caso erre sua conta será bloqueada")
                    elif tent == 2:
                        print("Sua conta foi bloqueada por várias tentativas erradas")
                        break
                    key = str(input(" "))
                    tent += 1
            novo_saque = int(input("Deseja realizar um novo saque:\n [1] - Sim\n [2] - Não\n "))
            if novo_saque == 1:
                print("Digite seu nome novamente:\n")
                lim_saque += 1
                tent = 0
            else:
                break
    else:
        print("Saldo Insuficiente")
        exit()
elif operacao == 3:
    print("========Extrato=======")
    print(f"Não ocorreu transações então o último deposíto foi de R${deposito:.2f}")
    print(f"Não ocorreu transações então o último saque foi de R${saque:.2f}")
    print(f"O saldo atual da conta é de R${saldo:.2f}")
