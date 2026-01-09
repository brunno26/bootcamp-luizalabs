nome = "Bruno"
idade = 23
profissao = "Telemarketing"
idioma = "Inglês"
salario = 18.345

#Forma não mais usada
print("Nome: %s Idade: %d Salário: %f" % (nome, idade, salario))

#Forma que pode ser usada
print("Nome: {} Idade: {} Salário: {}".format(nome, idade, salario))

# O fstring é o mais utilizado
print(f"Nome: {nome} Idade: {idade} Idioma: {idioma} Salario: {salario:.2f}")