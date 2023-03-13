print("liquidacion de salario")

nombre = input("ingrese nombre del empleado: ")
apellido = input("ingrese apellido del empleado: ")

horasTrabajadas = int(input("ingrese cantidad de horas trabajadas por el empleado: "))

valorHora = 650

premio = 5500

def calcular(horasTrabajadas, valorHora, premio):
    bruto = valorHora*horasTrabajadas

    if horasTrabajadas > 250:
        monto = bruto+premio

        print(f"{nombre} {apellido} usted trabajo {horasTrabajadas} horas y su salario mensual es de {monto}")
    
    else:

        print(f"{nombre} {apellido} usted trabajo {horasTrabajadas} horas y su salario mensual es de {bruto}")

calcular(horasTrabajadas, valorHora, premio)




