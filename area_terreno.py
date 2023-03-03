print("vamos a conocer su lote")

opcion = int(input("ingrese opcion de menu: "))

#menu de opciones
def menu():
    print("opcion 1: lote edificado")
    print("opcion 2: lote no edificado")
    print("opcion 3: salir")



#aqui vemos y calculamos el espacio libre de un terreno con edificacion
def edificado():
    if opcion == 1:
        print("edificado")
        print("ingrese medidas")

        frente = float(input("ingrese medida frente: "))
        fondo = float(input("ingrese medida fondo: "))

        print("medidas vivienda")

        f_vivienda = float(input("ingrese medida frente: "))
        lateral = float(input("ingrese medida lateral: "))

        total = (frente*fondo)-(f_vivienda*lateral)

        print(f"su terreno tiene un espacio libre de {total}")

#calculamos el area de un terreno vacio
def vacio():
    if opcion == 2:
        print("terreno sin edificar")

        frente = float(input("ingrese medida frente: "))
        fondo = float(input("ingrese medida fondo: "))

        total = frente*fondo

        print(f"su terreno esta vacio y mide {total}")


#salimos del programa
def salir():
    if opcion == 3:
      print("ha decidido salir. gracias por utilizar este programa")


      
#llamamos a las distintas funciones
menu() 
edificado()
vacio()
salir()
        

