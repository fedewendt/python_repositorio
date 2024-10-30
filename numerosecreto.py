import random

numero_secreto = random.randint(1, 100)

intentos = 0

adivinado = False

print("adivina el numero del 1 al 100")

while not adivinado:
    intento = int(input("dime un numero del 1 al 100: "))
    intento +=1



    if intento < numero_secreto:
        print("numero bajo")
    elif intento > numero_secreto:
        print("numero alto")
    else:
        adivinado = True
        print("numero correcto")

       
