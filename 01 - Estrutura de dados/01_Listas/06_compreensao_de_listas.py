
# Filtrar lista - Percorre todos os números da lista pegando somente os números pares (numero % 2 == 0) e monta uma nova lista somente com números pares.
numeros = [1, 30, 21, 2, 9, 65, 34]

# Crie uma nova lista para cada número dentro da lista números se o resto da divisão por 2 for igual a zero (par).
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


# Modificar valores - Percorre dos os números da lista elevando cada numero ao quadrado e criando uma nova lista com os valores modificados.
numeros = [1, 30, 21, 2, 9, 65, 34]

# Para cada número em números, pegue o número ao quadrado e adicione a lista.
quadrado = [numero**2 for numero in numeros]
print(quadrado)