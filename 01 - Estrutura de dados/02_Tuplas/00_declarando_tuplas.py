# Criação e acesso aos dados da tupla - irmã da lista
# Tuplas são estruturas de dados muito parecida como as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe "tuple" ou colocando valores separados por vírgula de parênteses.

# Métodos da classe tuple
# .count
# .index(value)
# .len


frutas = ("Laranja", "Pera", "Melancia",)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = tuple("Brasil",)
print(pais)