# É um conjunto não ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por {chaves}, e contém uma lista de pares chave:valor separadas por vírgula

# Exemplo criando um dicionário:
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

# Criando um dicionário usando a função dict
pessoa = dict(nome = "Guilherme", idade = 28)

#Forma de inserir uma informação em dicionário
pessoa ["telefone"] = "3373-1649"
print(pessoa)

# O dicionário não permite repetição de chaves, então, se for colocado outro valor para pessoa["nome"] = "Maria" ele vai sobrescrever o valor.
pessoa ["nome"] = "Maria"
print(pessoa)
