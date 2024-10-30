import random

numeros = [num for num in range(1, 25)]

sorteo = list()

cant = 15

while cant > 0:
    numero = random.choice(numeros)
    if numero not in sorteo:
        sorteo.append(numero)
        cant-=1
        
print(sorted(sorteo))
    

