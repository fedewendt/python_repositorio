empleado = input("ingrese el nombre del empleado: ")

sueldo = float(input("ingrese el sueldo anual del empleado: "))

promedio = sueldo/12

if promedio <= 300:
    print(f"el sueldo mensual promedio de {empleado} es {promedio} y es bajo")
elif promedio > 300 and promedio <= 900:
    print(f"el sueldo mensual promedio de {empleado} es {promedio} y es normal")
else:
    print(f"el sueldo mensual promedio de {empleado} es {promedio} y es mejor")

