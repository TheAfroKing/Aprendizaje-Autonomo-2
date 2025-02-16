# -*- coding: utf-8 -*-
'''
Piedra papel o tijera
'''
#Importacion de modulos re para valdiacion de expresiones regulares y random para la eleccion del sistema
import re
import random as rd


# Inicio la variable global de eleccion
eleccionJugador='null'

# Variables Pruebas
while eleccionJugador != 'Salir':
    #Reinicio de lapiedrpie eleccion
    eleccionJugador='null'
    print ("\n\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
    MMMMMM   ___  _            _                    ___                     _           _____  _   _                   MMMMM\n\
    MMMMMM  / _ \(_)  ___   __| | _ __  __ _       / _ \ __ _  _ __    ___ | |   ___   /__   \(_) (_)  ___  _ __  __ _ MMMMM\n\
    MMMMMM / /_)/| | / _ \ / _` || '__|/ _` |     / /_)// _` || '_ \  / _ \| |  / _ \    / /\/| | | | / _ \| '__|/ _` |MMMMM\n\
    MMMMMM/ ___/ | ||  __/| (_| || |  | (_| | _  / ___/| (_| || |_) ||  __/| | | (_) |  / /   | | | ||  __/| |  | (_| |MMMMM\n\
    MMMMMM\/     |_| \___| \__,_||_|   \__,_|( ) \/     \__,_|| .__/  \___||_|  \___/   \/    |_|_/ | \___||_|   \__,_|MMMMM\n\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xkONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKOOKWW0dlokkolOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKdodxookc'oNMMNdlXMMWNNNWMMMMMMMMMMMMMMMMMMMMMMMMMNOxkXMMMMMMMMMWWMMM\n\
    MMMMMMMMMMMMMMMMMMMNOxxxxxxOXMMMMMMMMMMMMMMMMMMMMMNolXMMNo'''dWMMWxlKW0ddxdd0WMMMMMMMMMMMMMMMMMMMMMMKookol0MMMMMMXxddd0W\n\
    MMMMMMMMMMN0OOOOO00olk0000OolKMMMWWMMMMMMMMMMWWWWMXldWMMMx..,xWMMWxlKkcxNWNdc0MMMMMMMMMMMMMMMMMMMMMNooXMXloNMMMW0loKXkck\n\
    WKkxxkkxkxloxkkkxd;,kWMMMMMO:cxxxxxxx0WMMMMXkdxddOKcoWMMMk..,xWMMWdlkcdWMMMOcOMMMMMMMMMMMMMMMMMMMMMOckMMWxcKMMM0ldNMMNol\n\
    kcxOOOOOx;cXMMMMMNc'kMMMMMM0;lKNNNNXdl0MMMXol0NNkcocoWMMMk..,xWMMWdcclKMMMWdcKMMMMMMMMMMMMMMMMMMMMWxcKMMMOcOMMXloNMMMKld\n\
    olNMMMMMNolXMMMMMNl'kMMMMMM0ckMMMMMM0ckMMMXloWMMNo::oNMMMk..;xMMMWd.,xWMMMKcdWMMMMMMMMMMMMMMMMMMMMNolXMMM0ckMWdlKMMMWxlK\n\
    olNMMMMMNolNMMMMMNl'kMMMMMM0ckMMMMMM0ckMMMNolXMMWx;,oNMMMO'.;kMMMWo.cXMMMWkcOMMMMMMMMMMMMMMMMMMMMMXloWMMM0cxWOckWMMMKlxW\n\
    olNMMMMMNolNMMMMMNl'kMMMMMM0ckMMMMMM0ckMMMMxc0MMMO,.lNMMMO'.:kMMMWo,OMMMMNolXMMMMMMMMMMMMMMMMMMMMMKcdWMMM0cxXooNMMMWdlKM\n\
    olNMMMMMNolNMMMMMNl'kMMMMMM0ckMMMMMM0ckMMMMOckMMMK:.lNMMMO'.:kMMMNolXMMMM0cxWMMMMMMMMMMMMMMMMMMMMMKcdWMMM0cxkcOMMMM0cxWM\n\
    olNMMMMMNolNMMMMMNl'kWMMMMM0ckMMMMMM0ckMMMMKcdWMMNl.cNMMM0''cOMMMNolXMMMWxcKMMMMMMMMMMMMMMMMMMMMWWKcxWMMMOcdloNMMMNdlXMM\n\
    olNMMMMMNolNMMMMMNl.:dxxxxko;dNWWMMM0ckMMMMNloNMMWd.;O0OOd..;oOOOk:cKWMMXloNMWX00KNMMMMMMMMMMW0xddl,dWMMMOcccOMMMM0ckWMM\n\
    dlKWWWWWXllNMMMMMNl.:OXK0kxdoodddxxko;dNWMMWdcKN0xl:ldxxxxdddxxxxxddddx0xcOWKdodxdoOWMWXkxxxkockXXk:oNMMMO;,dNMMMNolXMMM\n\
    0ccdxxxdo,lNMMMMMNl'kWMMMMMMMWWNK0OkxodddONMk:lookXWMMMMMMMMMMMMMMMMWXkl,c0klxXMMWdc0M0lo0K0l,oWMMWdcKMMMNxxXMMMMOckMMMM\n\
    NolKXXXXXdckXXXXXO;:KMMMMMMMMMMMMMMMMMMWxcOM0;,kWMMMMMMMMMMMMMMMMMMMMMMNx::l0WMMMXolXWdcKMMMKcdWMMWxcKMMMMMMMMMMNolXMMMM\n\
    WdlNMMMMMNkdxxxxxd:cONWMMMMMMMMMMMMMMMMWxcKMKcoNMMMMMMMMMMMMMMMMMMMMMMMMWd;OMMMMKooKMWdlXMMMKcdWMMWxcKMMMMMMMMMMOcOMMMMM\n\
    MxlKMMMMMMMMWWWWMWXkdddxxxkO0KXNWMMMMMMXldNMKcdWMMMMMMMMMMMMMMMMMMMMMMMMM0cxWMW0loXMMWdlXMMMKcdWMMWxc0NK0KXNWWMXloNMMMMM\n\
    MOcOMMMMMMMMMMMMMMMMWWNX0OkxxxddddxxkOOol0MMXloNMMMMMMMMMMMMMMMMMMMMMMMMMNdlKWOcdNMMMWxc0MMMO:dWMMWx,cddxxdddxxl;oXWMMMM\n\
    MXldWMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0d;cxOXWMMNolXMMMMMMMMMMMMMMMMMMMMMMMMMMKllxcxNMMMMMXo:oxdl;c0WWK:'dNMMMWWNXK0kdlkNMMM\n\
    MWxlKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKldWMMMMMWxcKMMMMMMMMMMMMMMMMMMMMMMMMMMMO,;kWMMMMMMMO:oO0XXkoddo::OMMMMMMMMMMMWkcOMMM\n\
    MMKlxWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0ckMMMMMMMkc0MMMMMMMMMMMMMMMMMMMMMMMMMMWx:kWMMMMMMMMOcOMMMMMNXXNXdlx0KXNWMMMMMNxc0MMM\n\
    MMWxc0MMMMMMMMMMMMMMMMMMMMMMMMMMMMNolXMMMMMMMOckMMMMMMMMMMMMMMMMMMMMMMMMMWOcxWMMMMMMMMMOckMMMMMMMMMMWKkxxddddxddxoo0WMMM\n\
    MMMNdl0MMMMMMMMMMMMMMMMMMMMMMMMMW0ooKMMMMMMMMXooXMMMMMMMMMMMMMMMMMMMMMMMNxlkNMMMMMMMMMMXldWMMMMMMMMMMMMMMWWNX0c:kXWMMMMM\n\
    MMMMNxlxKXXXXXXXXXXXXXXXXXXXXKOxddONMMMMMMMMMMKooKWMMMMMMMMMMMMMMMMMMMNOoo0WMMMMMMMMMMMWkcOWMMMMMMMMMMMMMMMMMKldWMMMMMMM\n\
    MMMMMWKkxkkkkkkkkkkkkkkkkxkkxxxOKWMMMMMMMMMMMMMXxodOKNWWWWWWWWWWWWWX0xodOWMMMMMMMMMMMMMMWkldKNWWWWMMMMMWWWNKkooKMMMMMMMM\n\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOxdddddddddddddddddkKWMMMMMMMMMMMMMMMMMWXkdxxxxxxxxxxxxxxxx0NMMMMMMMMM\n\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNNNNNNNNNNNNWMMMMMMMMMMMMMMMMMMMMMMMMMWWNNNXXKXXXNNWMMMMMMMMMMMMM")
    
    
    # Inicio la variable de la expresion regular para validar las 3 opciones
    expresionRegular = r"^Piedra$|^Papel$|^Tijera$|^Salir$"
    
    # Mientras la opcion no sea valido sigo solicitando
    while not re.findall(expresionRegular, eleccionJugador):
        # Solicito que el usuario ingrese una de las 3 opciones y le pongo la primera letra en May y lo guardo en la variable global eleccion
        eleccionJugador = input('Escriba alguna de las opciones Piedra/Papel/Tijera\nEscriba Salir para terminar el juego: ').capitalize()
        # Si no es valido se muestra el mensaje de opción válida
        if not re.findall(expresionRegular, eleccionJugador):
            print('Seleccione una opcián válida')
        pass
    if eleccionJugador != 'Salir':
        # Se define un array de las opciones para cuando se genere un numero aleatorio entre 0 y 2 se use el indice para seleccionar entre piedra papel o tijera
        opciones=['Piedra','Papel','Tijera']
        # Se obtiene el valor random entre 0-2 para que utilice el indice del array
        eleccionDelSistema=opciones[rd.randrange(0,3,1)]

        # Mostramos el mensaje para que el jugador sepa que eligió el sistema
        print('El sistema eligió: '+eleccionDelSistema)


        #Valido los resultados
        if eleccionJugador == eleccionDelSistema:
            print('Empate')
        else:
            match eleccionDelSistema:
                case 'Piedra':
                    if eleccionJugador == 'Papel':
                        print('Ganador: Jugador')
                    else:
                        print('Ganador: Sistema')
                case 'Papel':
                    if eleccionJugador == 'Tijera':
                        print('Ganador: Jugador')
                    else:
                        print('Ganador: Sistema')
                case 'Tijera':
                    if eleccionJugador == 'Piedra':
                        print('Ganador: Jugador')
                    else:
                        print('Ganador: Sistema')
        eleccionJugador = input('Precione enter para seguir jugando o escriba salir para terminar el juego: ').capitalize()
