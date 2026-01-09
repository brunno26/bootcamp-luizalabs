# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve pular no acesso.

lista = ["p", "y", "t", "h", "o", "n"]

# Pega do índice 2 até o final.
print(lista[2:])

# Pega do início até o índice 1 (antes do 2)
print(lista[:2])

# Pega do índice 1 até o indice 2 (antes do 3)
print(lista[1:3])

# Pega do índice 0 até o 2, pulando de 2 em 2
print(lista[0:3:2])

# Pega toda a lista do começo ao fim
print(lista[::])

# Pega a lista toda ao contrário
print(lista[::-1])