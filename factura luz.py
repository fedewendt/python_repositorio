print("Factura de electricidad")


def menu():
    print("opcion 1: tarifa residencial")
    print("opcion 2: tarifa comercial")
    print("opcion 3: salir")

    
menu()


#el periodo que se toma entre lecturas es bimestral pero despues se facturara mensual
#es valido en tarifa comercial o residencial


opcion = int(input("ingrese una opcion del menu (en numero): "))

if opcion == 1:
    print("tarifa residencial")

    lectura_anterior = int(input("ingrese lectura periodo anterior: "))
    lectura_actual = int(input("ingrese lectura periodo anterior: "))

    consumo = lectura_actual - lectura_anterior
    precio_kw = 4.47

    cargos = {"cargo fijo" : 61.44 , "impuesto" : 1.21 , "Alum PB" : 950}
    

    for i in cargos:
        subtotal = (cargos[i])

    monto = precio_kw * consumo + subtotal

    monto_mens = monto / 2

    if consumo <= 400:
        bonif = 250
        tot_mens = monto_mens - bonif

#monto_mens = monto mensual
#tot_mens = total mensual
#bonif = bonificacion

    
        print(f"su factura es de {consumo}kw, tiene ahorro y debe abonar ${tot_mens}")

    else:
        print(f"su factura es de {consumo}kw, esta excedido y debe abonar ${monto_mens}")


elif opcion == 2:
    print("tarifa comercial")
    lectura_anterior = int(input("ingrese lectura periodo anterior: "))
    lectura_actual = int(input("ingrese lectura periodo actual: "))
    consumo = lectura_actual - lectura_anterior
    precio_kw = 7.54

    cargos = {"cargo fijo" :85.22 , "ing bruto" : 0.25 , "IVA" : 1.21 , "alum pb" : 1010}

    for i in cargos:
        subtotal = (cargos[i])

    monto = precio_kw * consumo + subtotal

    monto_mens = monto / 2

    if consumo <= 500:
        bonif = 180
        tot_mens = monto_mens - bonif


        print(f"su factura es de {consumo}kw, tiene ahorro y debe abonar ${tot_mens}")

    else:
        print(f"su factura es de {consumo}kw, esta excedido y debe abonar ${monto_mens}")

else:
    print("usted decidio salir. gracias por utilizar el programa")
