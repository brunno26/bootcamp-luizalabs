# Permite escrever uma condição em uma única linha de código. É composta por três partes: a condição, o valor retornado se a condição for verdadeira e o valor retornado se a condição for falsa.

saldo = 1000
saque = 1500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque.")