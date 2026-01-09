# O comando while é usado para repetir um bloco de código várias vezes enquanto uma condição lógica for alcançada. Ele é usado quando não sabemos o numero exatos de iterações que queremos fazer.

opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar\n [2]Extrato\n [0]Sair\n"))
    
    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2:
        print("Exibindo extrato...")
        

# Exemplo de uso do while com else
while opcao != 0:
    opcao = int(input("[1]Sacar\n [2]Extrato\n [0]Sair\n"))
    
    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Obrigado por usar nosso sistema!") 