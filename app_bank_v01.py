
style =["*************************************", ""]
list_op = ["[D] Depositar ", "[S] Sacar ", "[E] Extrado "]

#saldo inicial da conta
saldo = 0

#limite monetário de saque 
limite = 500

#extrado inical da conta
extrato = ""

#numero de operações de saque
n_op_saque = 0

#limite de movimentações diárias
limite_saque = 3

print(style[0])
print(style[1])
print("--- SISTEMA BANCÁRIO v1.0 ---")
print(style[1])
print(style[0])

print(style[1])
#escolha do user para iniciar ou encerrar o sistema
init_sys = input("Digite \'I\' para Iniciar o Sistema e/ou Digite \'P\' para Encerrar o Sistema. ").upper()
print(style[1])

print(style[0])
print(style[1])
print("Bem-Vindo")
print(style[1])

while init_sys == "I":

    print(style[0])
    print(style[1])
    print("Lista de operações: ")
    print(style[1])
    
    #listar operações disponiveis
    for i in list_op:
        print(i)
    
    print(style[1])
    print(style[0])
    print(style[1])

    op = input("Escolha a operação desejada [D] [S] [E]. Se desejar encerrar o programa digite \"Q\": \n").upper()
    print(style[1])
    print(style[0])

    #operação de deposito
    if op == "D":
        print(style[1])
        valor = float(input("Informe o valor a ser depositado: "))
        print(style[1])
        
        if valor > 0:
            saldo += valor
            extrato += f"Déposito realizado: R$ {valor:.2f}\n"
        else:
            print(style[1])
            print("A operação falhou! O valor informado é invalido!")
            print(style[1])

    #operação de saque
    elif op == "S":
        print(style[1])
        valor = float(input("Informe o valor à ser sacado: "))
        print(style[1]) 

        ex_saldo = valor > saldo
        ex_limit = valor > limite
        ex_saque = n_op_saque >= limite_saque

        if ex_saldo:
            print(style[1])
            print("Operação invalida! Você não possui saldo suficiente. ")
            print(style[1])
        
        elif ex_limit:
            print(style[1])
            print("Operação invalida! Limite de saque excedido. ")
            print(style[1])

        elif ex_saque:
            print(style[1])
            print("Operação invalida! Limite de saques diários excedido")
            print(style[1])

        elif saldo > 0:
            saldo -= valor
            extrato += f"Saque realizado: R$ {valor:.2f}\n"
            n_op_saque += 1

        else:
            print(style[1])
            print("Operação invalida! Valor informado invalido. ")
            print(style[1])

    #operação "Exibir" extrado
    elif op == "E":
        print(style[0])
        print(style[1])
        print("Não há movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(style[1])
        print(style[0])

    # parar sistema 
    elif op == "Q":
        break

    else:
        print(style[1])
        print("Operação invalida! Informe novamente qual operação deseja realizar ")
        print(style[1])
