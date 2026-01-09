# .sorted() é usado para ordenar iteráveis

linguagens = ["python", "js", "c", "java", "csharp"]

# ordena por ordem alfabética
print(sorted(linguagens, key=lambda x:len(x)))

# ordena de trás para frente
print(sorted(linguagens, key=lambda x:len(x), reverse=True))