menu = """

[1] Deposito
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_depositos = []
lista_saques =[]

while True:

    opcao = input(menu)
        
    
    if opcao == "1":
        
        pre_saldo = float(input("Informe o valor a ser depositado "))
        
        
        
        if pre_saldo > 0:
            saldo += pre_saldo
            lista_depositos.append(pre_saldo)

        else:
            print("Valor do deposito Invalido ")
            print()   

    elif opcao == "2":
        pre_saque =float(input("Informe o valor a ser Sacado "))



        if saldo <=0:
            print("Seu saldo e insuficiente ")
            print()
        
        elif numero_saques >=LIMITE_SAQUES:
            print("Voce nao pode mais realizar saques hoje ")
            print()



        elif pre_saque > limite:
            print("Voce ultrapassou o limite de saque de R$ 500,00 ")
            print()
                      
        elif pre_saque > 0:
                saldo -= pre_saque
                numero_saques += 1
                lista_saques.append(pre_saque)
                
        else:
            print("Valor Invalido..")    
        

        

    elif opcao == "3":
        print("Seu extrato sera mostrado abaixo..")
        print(f" Seu saldo e de ","R$ {:,.2f}".format(float(saldo)), ".")
        print(f"Voce pode realizar {LIMITE_SAQUES-numero_saques} saques hoje. ")


        for indice, lista_deposito in enumerate(lista_depositos):
            print(f" Voce realizou os seguintes depositos",indice,"R$ {:,.2f}".format(float(lista_deposito)))

        for indice, lista_saque in enumerate(lista_saques):
            print(f" Voce realizou os seguintes saques",indice,"R$ {:,.2f}".format(float(lista_saque)))
    
    elif opcao == "0":
        break

    else:
        print("Operacao invalida, por favor selecione novamente a operacao desjada.")
        print()