print("app para saber el clima en determinada ciudad")

import requests

ciudad = input("ingrese su ciudad: ")

def obtener_temperatura(ciudad):
    url = "http://wttr.in/" + ciudad + "?format=3"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        print(respuesta.text)
    else:
        print("error. ciudad no encontrada")


obtener_temperatura(ciudad)

