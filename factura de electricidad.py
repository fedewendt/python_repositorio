print('=== CALCULADORA EDESUR===')
print('')

lectura_anterior = int(input('Lectura anterior: '))
lectura_actual = int(input('Lectura actual: '))

consumo = lectura_actual - lectura_anterior

# Montos noviembre 2026 - R1 con subsidio
cargo_fijo = 1826.26
precio_sin_subsidio = 161.157
precio_con_subsidio = precio_sin_subsidio * 0.25  # $40,29

print('')
print(f'Consumo: {consumo} kWh')

if consumo <= 200:
    con_sub = consumo
    sin_sub = 0
else:
    con_sub = 200
    sin_sub = consumo - 200

monto_variable = (con_sub * precio_con_subsidio) + (sin_sub * precio_sin_subsidio)
total = monto_variable + cargo_fijo

print(f'Con subsidio: {con_sub} kWh x ${precio_con_subsidio:.2f} = ${con_sub * precio_con_subsidio:.2f}')
print(f'Sin subsidio: {sin_sub} kWh x ${precio_sin_subsidio:.2f} = ${sin_sub * precio_sin_subsidio:.2f}')
print(f'Cargo fijo: ${cargo_fijo:.2f}')
print(f'---------------------------')
print(f'TOTAL A PAGAR: ${total:.2f}')