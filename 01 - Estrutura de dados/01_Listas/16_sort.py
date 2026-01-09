# é usado para ordenar nossa lista

linguagens = ["python", "js", "c", "java", "csharp"]

# ordena por ordem alfabética
linguagens.sort()
print(linguagens)

# ordena de trás para frente
linguagens.sort(reverse=True)
print(linguagens)

# retorna pelo tamanho da string// Lambda é uma função anônima
linguagens.sort(key=lambda x:len(x))
print(linguagens)

# retorna pelo tamanho da string ao contrário
linguagens.sort(key=lambda x:len(x), reverse=True)
print(linguagens)