print('hola')

print('vamos a conocer su edad')

nombre = input('diga su nombre: ')

edad = int(input('diga su edad: '))

if edad >= 18:
	print(f'bienvenido {nombre} usted tiene {edad} años y es mayor')

	
else:
	print(f'{nombre} usted tiene {edad} años y es menor')