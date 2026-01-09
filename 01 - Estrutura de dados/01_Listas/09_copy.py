# .copy() a lista é um objeto mutavel e quando ela é passada para outra pessoa usar em outra parte do código o que é feito na lista é refletido. Então podemos fazer o uso de .copy() para retornar uma lista igual, porém, com uma instância diferente.

lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)