#titulo
print('horas trabajadas')

#pide el nombre del empleado
nombre=input('ingrese nombre del emplado: ')

#pide el valor hora
valor_hora=float(input('ingrese valor hora: '))

#pide cantidad de horas trabajadas
horas_trabajadas=int(input('ingrese cantidad de horas trabajadas: '))


#calcula el monto
monto=valor_hora*horas_trabajadas


#decide si el empleado gana bien o mal
if monto <0:
	print(f'{nombre} esta en deficit')
elif monto < 300000:
	print(f'{nombre} gana poco')
elif monto == 300000:
	print(f'{nombre} gana bien')
else:
	print(f'{nombre} tiene un sueldo excelente')