
# ==========================================
# SISTEMA DE FACTURACION DEL SERVICIO ELECTRICO

# ==========================================

print("======================================")
print("   FACTURACION DEL SERVICIO ELECTRICO")
print("======================================")

# 1. INGRESO DE DATOS DEL CLIENTE

nombre = input("Ingrese el nombre del cliente: ")
numero = input("Ingrese el numero de cliente: ")

# 2. INGRESO DEL CONSUMO ELECTRICO

lectura_anterior = int(input('ingrese lectura anterior: '))
lectura_actual = int(input('ingrese lectura actual: '))

consumo = lectura_actual - lectura_anterior

# 3. VALIDACION DEL CONSUMO

if consumo < 0:
    print("Error: el consumo no puede ser negativo.")

else:

    # 4. DEFINICION DE TARIFAS

    precio_kwh = 157.13
    cargo_fijo = 3632.46
    porcentaje_impuesto = 0.21

    # 5. CALCULO DE LOS IMPORTES

    importe_consumo = consumo * precio_kwh

    subtotal = importe_consumo + cargo_fijo

    impuesto = subtotal * porcentaje_impuesto

    total = subtotal + impuesto

    # 6. GENERACION DE LA FACTURA

    print("\n")
    print("======================================")
    print("          FACTURA DE ELECTRICIDAD")
    print("======================================")

    print("Cliente:", nombre)
    print("Numero de cliente:", numero)

    print("--------------------------------------")
    print("DETALLE DE FACTURACION")
    print("---------------------------------------")
    
    print(f'Lectura anterior: {lectura_anterior} ')
    print(f'Lectura actual: {lectura_actual}')

    print("Consumo:", consumo, "kWh")
    print("Precio por kWh: $", precio_kwh)
    print("Importe de consumo: $", round(importe_consumo, 2))
    print("Cargo fijo: $", cargo_fijo)
    print("Subtotal: $", round(subtotal, 2))
    print("Impuesto (21%): $", round(impuesto, 2))

    print("--------------------------------------")
    print("TOTAL A PAGAR: $", round(total, 2))
    print("======================================")
    print("Gracias por utilizar nuestro servicio")
