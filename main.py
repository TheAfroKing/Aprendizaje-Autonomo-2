# -*- coding: utf-8 -*-
"""
Piedra papel o tijera
"""
#Importacion de modulos re para valdiacion de expresiones regulares y random para la eleccion del sistema
import re
import random as rd



# Variables Pruebas
"""
a=2
b=3
result = 2 ** 3
result2 = (a+5)/(b-1)
"""

# Inicio la variable global de eleccion
eleccionJugador='null'
# Inicio la variable de la expresion regular para validar las 3 opciones
expresionRegular = r'^Piedra$|^Papel$|^Tijera$'

# Mientras la opcion no sea valido sigo solicitando
while not re.findall(expresionRegular, eleccionJugador):
    # Solicito que el usuario ingrese una de las 3 opciones y le pongo la primera letra en May y lo guardo en la variable global eleccion
    eleccionJugador = input("Escriba alguna de las opciones Piedra/Papel/Tijera: ").capitalize()
    # Si no es valido se muestra el mensaje de opción válida
    if not re.findall(expresionRegular, eleccionJugador):
        print("Seleccione una opcián válida")
    pass

# Se define un array de las opciones para cuando se genere un numero aleatorio entre 0 y 2 se use el indice para seleccionar entre piedra papel o tijera
opciones=["Piedra","Papel","Tijera"]
# Se obtiene el valor random entre 0-2 para que utilice el indice del array
eleccionDelSistema=opciones[rd.randrange(0,3,1)]

# Mostramos el mensaje para que el jugador sepa que eligió el sistema
print("El sistema eligió: "+eleccionDelSistema)


#Valido los resultados
if eleccionJugador == eleccionDelSistema:
    print("Empate")
else:
    match eleccionDelSistema:
        case "Piedra":
            if eleccionJugador == "Papel":
                print("Ganador: Jugador")
            else:
                print("Ganador: Sistema")
        case "Papel":
            if eleccionJugador == "Tijera":
                print("Ganador: Jugador")
            else:
                print("Ganador: Sistema")
        case "Tijera":
            if eleccionJugador == "Piedra":
                print("Ganador: Jugador")
            else:
                print("Ganador: Sistema")
