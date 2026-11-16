nombre=input('ingrese nombre del cliente:  ')

anterior=int(input('ingrese lectura anterior: '))

actual=int(input('ingrese lectura actual: '))

def facturar(nombre, anterior, actual):
    consumo = actual - anterior

    cargo_fijo = 1500
    precio_m3 = 250

    subtotal = cargo_fijo + (consumo * precio_m3)
    iva = subtotal * 0.21
    total = subtotal + iva

    print(f"Cliente: {nombre}")
    print(f"Consumo: {consumo} m3")
    print(f"Total a pagar: ${total:.2f}")
    return total

facturar(nombre,anterior,actual)