# São utilizadas para repetir um bloco de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado por meio de uma expressão lógica.
# Em Python, as estruturas de repetição mais comuns são o "for" e o "while".
# O comando for é usado para percorrer um objeto iterável(listas, tuplas, dicionários). Ele é usado quando sabemos o número de iterações que queremos fazer.

# Exempo usando um iterável
texto = input("Digite um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
print()


# A função range é usada para gerar uma sequencia de números inteiros. Ele recebe 3 argumentos: start, stop e step.
# Exemplo usando a função range

for numero in range(1, 11):
    resultado = numero * 5
    print(f"{numero} x 5 = {resultado}")