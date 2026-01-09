# Condicional Simples: Verifica se a idade é suficiente para tirar a carteira de motorista.
MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Digite a sua idade:"))

if idade >= MAIOR_IDADE:
    print("Elegível para tirar a carteira de motorista.")
    
if idade < MAIOR_IDADE:
    print("Não é elegível para tirar a carteira de motorista.")


# Condicional Composta: Verifica se a idade é suficiente para tirar a carteira de motorista.
if idade >= MAIOR_IDADE:
    print("Elegível para tirar a carteira de motorista.")
else:
    print("Não é elegível para tirar a carteira de motorista.")
    

# Condicional Encadeada: Verifica diferentes condições de elegibilidade para a carteira de motorista.
if idade >= MAIOR_IDADE:
    print("Elegível para tirar a carteira de motorista.")
elif idade == IDADE_ESPECIAL:
    print("Elegível para fazer aulas téóricas mas não aulas práticas.")
else:
    print("Não é elegível para tirar a carteira de motorista.")