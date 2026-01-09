# Formatando strings
nome = "Bruno"

print(nome.upper())
print(nome.lower())
print(nome.title())

# Eliminando os espaços em branco
texto = "  Bom dia!  "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

# Junção e Centralização
menu = "Python"

print("****" + menu + "****")
print(menu.center(14))
print(menu.center(20, "*"))
print("-".join(menu))
