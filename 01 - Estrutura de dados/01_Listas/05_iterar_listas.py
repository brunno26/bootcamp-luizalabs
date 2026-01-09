#A forma mais comum de percorrer os dados de uma lista é utilizando o comando "for".

carros = ["Gol", "Celta", "Pálio"]
# Neste código o comando percorre cada elemento da lista carros e a cada volta no loop, a variável "carro" recebe um dos valores da lista.
for carro in carros:
    print(carro)
    
# Neste código o enumerate (carros) devolve tanto o índice quanto o valor. Ou seja, indice recebe a posição e carro recebe o nome da lista 
for indice, carro in enumerate (carros):
    print(f"{indice}: {carro}")