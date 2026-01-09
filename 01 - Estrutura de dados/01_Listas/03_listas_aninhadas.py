# Lista aninhadas são matrizes e podem armazenar todos os tipos de objetos Python, portanto, podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais(tabelas) e acessar informando os indices de outra coluna.
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
    
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

