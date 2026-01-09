while True:
    numero = int(input("Digite um número:"))
    
    if numero == 10:
        break
    
    print(numero)
    
    
for numero in range(100):
    
    if numero == 10:
        break
    
    print(numero, end=" ")
    

while True:
    numero = int(input("Digite um número:"))
    
    if numero == 10:
        break
    
    if numero % 2 == 0:
        continue
    
    print(numero)