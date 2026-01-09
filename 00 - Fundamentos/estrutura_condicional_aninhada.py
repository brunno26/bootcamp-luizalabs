# Estrutra de decisão com condicional aninhada
conta_normal = False
conta_universitaria = False
saldo = 1000
saque = 1500
cheque_especial = 200

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial.")
    else:
        print("Saldo insuficiente para saque")
        
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente para saque")
else:
    print("O sistema não identificou o tipo de conta. Entre em contato com sua agência.")