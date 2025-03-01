# -*- coding: utf-8 -*-
'''
Piedra papel o tijera
'''
#Importacion de modulos re para validación de expresiones regulares y random para la elección del sistema
import re
import random as rd
import json
import getpass

#Fuente: https://stackoverflow.com/questions/8924173/how-can-i-print-bold-text-in-python
class colores:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

"""
    Función que maneja el menú principal del juego.
    Muestra las opciones disponibles y redirige al usuario a las funciones correspondientes
    según la opción seleccionada.
    
    Parámetros de entrada:
        Ninguno.
        
    Parámetros de salida:
        Ninguno.
"""
def menuPrincipal():
    # Inicio la variable de elección
    eleccionMenu='null'
    while eleccionMenu != 'Salir':
        
        #Reinicio de la elección
        eleccionMenu='null'
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
        #Se declaran las opciones del menú principal
        opciones=["Reglas","Contra la computadora","Multijugador (2 jugadores)","Ver estadísticas","Salir"]
        imprimirMenus('Principal',opciones)
        eleccionMenu=entradaMenus(opciones)
        match eleccionMenu:
            case 'Reglas':
                reglas()
            case 'Contra la computadora':
                menuJuegoContraSistema()
            case 'Multijugador (2 jugadores)':
                menuJuegoMultijugador()
            case 'Ver estadísticas':
                menuEstadisticas()
                
"""
    Función que imprime dinámicamente los menús y submenús del juego.
    
    Parámetros de entrada:
        - menu (str): Nombre del menú que se va a imprimir.
        - opciones (list): Lista de opciones disponibles en el menú.
        
    Parámetros de salida:
        Ninguno.
"""  
def imprimirMenus(menu,opciones):
    print(f'\n\n{colores.BOLD}Menú: {menu}{colores.END}')
    # Creo automaticamente el menú basado en el indice de la array como opción y el valor como texto
    for i in range(len(opciones)):
        print(f"{colores.GREEN}{colores.BOLD}{i}:{colores.END}{colores.END} {opciones[i]}")

"""
    Función que solicita y valida la entrada del usuario en los menús.
    Asegura que la entrada sea un número válido dentro del rango de opciones.
    
    Parámetros de entrada:
        - opciones (list): Lista de opciones disponibles en el menú.
        
    Parámetros de salida:
        - str: Opción seleccionada por el usuario.
"""
def entradaMenus(opciones):
    largo=len(opciones)-1
    while True:
        entradaMenu=input(f"Ingrese un numero del (0-{largo}): ")
        try:
            entradaMenu=int(entradaMenu)
            if entradaMenu>=0 and entradaMenu<=largo:
                #print(opciones[entradaMenu])
                return opciones[entradaMenu]
            else: 
                print(f"{colores.RED}Opción incorrecta, inténtelo de nuevo.{colores.END}")
        except:
            print(f"{colores.RED}Solo se aceptan números enteros, inténtelo de nuevo.{colores.END}")

"""
    Función que muestra las reglas del juego y las instrucciones para los modos de juego.
    Puede llamar a una función de callback después de mostrar las reglas.
    
    Parámetros de entrada:
        - callback (str/func): Función a la que se llamará después de mostrar las reglas.
        Por defecto es 'null'.
        - nroDeJugadores (int): Número de jugadores (0, 1 o 2) para mostrar reglas específicas.
        Por defecto es 0.
        
    Parámetros de salida:
        Ninguno.
"""
def reglas(callback='null',nroDeJugadores=0):
    print(f"\n\n{colores.BOLD}Reglas básicas{colores.END}\n\
    {colores.BOLD}Objetivo:{colores.END} El objetivo del juego es vencer a tu oponente eligiendo la opción que supera a la suya.\n\
    {colores.BOLD}Opciones:{colores.END}\n\
    {colores.BOLD}Piedra:{colores.END} Representada por un puño cerrado.\n\
    {colores.BOLD}Papel:{colores.END} Representado por la mano extendida, con la palma hacia abajo o hacia arriba.\n\
    {colores.BOLD}Tijera:{colores.END} Representada por los dedos índice y medio extendidos, formando una 'V'.\n\
    {colores.BOLD}Relaciones de fuerza:{colores.END}\n\
    - La piedra aplasta la tijera (la piedra gana a la tijera).\n\
    - La tijera corta el papel (la tijera gana al papel).\n\
    - El papel envuelve la piedra (el papel gana a la piedra).\n\
    - Empate: Si ambos jugadores eligen la misma opción, la ronda termina en empate y se vuelve a jugar.\n\
    \n")
    if nroDeJugadores==1 or nroDeJugadores==0:
        print(f"{colores.BOLD}Modo contra la computadora{colores.END}\n\
    - El jugador elige una de las tres opciones: piedra, papel o tijera.\n\
    - La computadora elige una opción al azar.\n\
    - Se comparan las opciones según las relaciones de fuerza mencionadas anteriormente.\n\
    - Se determina el ganador de la ronda jugador, computadora o empate).\n\
    - Se pueden jugar varias rondas para determinar un ganador final.\n\
    \n")
    if nroDeJugadores==2 or nroDeJugadores==0:
        print(f"{colores.BOLD}Modo Multijugador (2 jugadores){colores.END}\n\
    - Dos jugadores se enfrentan.\n\
    - Ambos jugadores eligen una de las tres opciones: piedra, papel o tijera.\n\
    - Se comparan las opciones según las relaciones de fuerza.\n\
    - Se determina el ganador de la ronda (jugador 1, jugador 2 o empate).\n\
    - Se pueden jugar varias rondas para determinar un ganador final.")
    
    pausa()
    if(callback!='null'):
        callback()

"""
    Función que maneja el submenú de juego contra la computadora.
    Muestra las opciones disponibles y redirige al usuario a las funciones correspondientes.
    
    Parámetros de entrada:
        Ninguno.
        
    Parámetros de salida:
        Ninguno.
"""
def menuJuegoContraSistema():
    opciones=["Ver Reglas","Jugar Contra la computadora","Ver estadísticas","Regresar al menú principal"]
    imprimirMenus('Contra la computadora',opciones)
    eleccionMenu=entradaMenus(opciones)
    match eleccionMenu:
        case 'Ver Reglas':
            reglas(menuJuegoContraSistema,1)
        case 'Jugar Contra la computadora':
            juegoContraSistema()
        case 'Regresar al menú principal':
            menuPrincipal()
        case 'Ver estadísticas':
            menuEstadisticas()

"""
    Función que maneja el submenú de juego multijugador (2 jugadores).
    Muestra las opciones disponibles y redirige al usuario a las funciones correspondientes.
    
    Parámetros de entrada:
        Ninguno.
        
    Parámetros de salida:
        Ninguno.
"""
def menuJuegoMultijugador():
    opciones=["Ver Reglas","Jugar Multijugador (2 jugadores)","Ver estadísticas","Regresar al menú principal"]
    imprimirMenus('Multijugador (2 jugadores)',opciones)
    eleccionMenu=entradaMenus(opciones)
    match eleccionMenu:
        case 'Ver Reglas':
            reglas(menuJuegoMultijugador,2)
        case 'Jugar Multijugador (2 jugadores)':
            juegoMultijugador()
        case 'Regresar al menú principal':
            menuPrincipal()
        case 'Ver estadísticas':
            menuEstadisticas()

"""
    Función que pausa la ejecución del programa hasta que el usuario presione Enter.
    Útil para permitir que el usuario lea la salida antes de continuar.
    
    Parámetros de entrada:
        Ninguno.
        
    Parámetros de salida:
        Ninguno.
    """
def pausa():
    input('Presione enter para volver al menú.')


"""
    Función que maneja el submenú de estadísticas del juego.
    Muestra las opciones disponibles y redirige al usuario a las funciones correspondientes.
    
    Parámetros de entrada:
        Ninguno.
        
    Parámetros de salida:
        Ninguno.
"""
def menuEstadisticas():
    opciones=["Ver estadísticas","Ver Historial","Limpiar estadísticas","Regresar al menú principal"]
    imprimirMenus('Estadistaicas',opciones)
    eleccionMenu=entradaMenus(opciones)
    match eleccionMenu:
        case 'Ver estadísticas':
            estadisticas()
        case 'Ver Historial':
            historial()
        case 'Limpiar estadísticas':
            #Trunco y abro el archivo
            open('./resultados.log','w').close()
        case 'Regresar al menú principal':
            menuPrincipal()

"""
    Función que calcula y muestra las estadísticas de las partidas jugadas.
    Lee los resultados desde el archivo 'resultados.log' y muestra el número de victorias,
    derrotas y empates para cada jugador.
    
    Parámetros de entrada:
        Ninguno.
        
    Parámetros de salida:
        Ninguno.
""" 
def estadisticas():
    partidas=[]
    with open('./resultados.log', 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            try:
                jugada=json.loads(linea.strip())
                partidas.append(jugada)
            except:
                print("Error en el archivo")
                open('./resultados.log','w').close()

    reglas = {
        "Piedra": "Tijera",
        "Tijera": "Papel",
        "Papel": "Piedra"
    }
    
    resultados = {}
    
    for partida in partidas:
        jugador1, jugador2 = partida  # Se asume que siempre hay dos jugadores en cada partida
        nombre1, eleccion1 = jugador1["nombre"], jugador1["eleccion"]
        nombre2, eleccion2 = jugador2["nombre"], jugador2["eleccion"]
        
        # Inicializar en el diccionario si no existe
        if nombre1 not in resultados:
            resultados[nombre1] = {"ganadas": 0, "perdidas": 0,"empate":0}
        if nombre2 not in resultados:
            resultados[nombre2] = {"ganadas": 0, "perdidas": 0,"empate":0}
        
        # Determinar el resultado de la partida y los guardo en la variable de resultados
        if eleccion1 == eleccion2:
            resultados[nombre1]["empate"] += 1
            resultados[nombre2]["empate"] += 1
        elif reglas[eleccion1] == eleccion2:
            resultados[nombre1]["ganadas"] += 1
            resultados[nombre2]["perdidas"] += 1
        else:
            resultados[nombre2]["ganadas"] += 1
            resultados[nombre1]["perdidas"] += 1
    #Muestro todos los resultados de todos los jugadores
    for jugador, stats in resultados.items():
        print(f"Jugador {jugador}: {stats['ganadas']} Ganadas y {stats['perdidas']} Perdidas y {stats['empate']} Empates")
    pausa()

"""
    Función que muestra el historial de partidas jugadas.
    Lee los resultados desde el archivo 'resultados.log' y los muestra en pantalla.
    
    Parámetros de entrada:
        Ninguno.
        
    Parámetros de salida:
        Ninguno.
"""
def historial():
    #Leo todas las lineas del archivo y valido y muestro los resultados
    with open('./resultados.log', 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            try:
                jugada=json.loads(linea.strip())
                validarResultados(jugada,False)
            except:
                open('./resultados.log','w').close()
    pausa()

"""
    Función que solicita y valida el nombre del jugador.
    Asegura que el nombre solo contenga letras y tenga una longitud entre 1 y 10 caracteres.
    
    Parámetros de entrada:
        Ninguno.
        
    Parámetros de salida:
        - str: Nombre del jugador validado.
"""
def solicitarNombre():
    nombre=input("Escriba su nombre (solo letras min:1 - max :10): ")
    while not re.match(r"^[A-Za-z]{1,10}$", nombre):
        nombre=input(f"Escriba su nombre ({colores.RED}solo letras min:1 - max :10{colores.END}): ")
    return nombre

   
"""
    Función que maneja la lógica del juego contra la computadora.
    Solicita el nombre del jugador, su elección y genera una elección aleatoria para la computadora.
    Luego, valida los resultados y los guarda en el archivo 'resultados.log'.
    
    Parámetros de entrada:
        Ninguno.
        
    Parámetros de salida:
        Ninguno.
"""
def juegoContraSistema():
    nombreJugador=solicitarNombre()
    jugadores=[
        {'nombre':nombreJugador,'eleccion':'null'},
        {'nombre':'Sistema','eleccion':'null'},
        ]
    partidas=0
    while partidas<=0:
        try:
            partidas=int(input('Ingrese el número de partidas que quiere jugar mayor a 0: '))
        except:
            print('Solo se permiten numeros.')
            partidas=int(input('Ingrese el número de partidas que quiere jugar mayor a 0: '))
    for partida in range(partidas):
        print(f'Partida: {partida+1}')
        #Se llama la función para que el jugador seleccione entre PPT
        seleccionarPPT(jugadores[0])
        # Se define un array de las opciones para cuando se genere un numero aleatorio entre 0 y 2 se use el indice para seleccionar entre piedra papel o tijera
        opciones=['Piedra','Papel','Tijera']
        # Se obtiene el valor random entre 0-2 para que utilice el indice del array
        jugadores[1]['eleccion']=opciones[rd.randrange(0,3,1)]
        #Se validan los resultados
        validarResultados(jugadores)

"""
    Función que maneja la lógica del juego multijugador (2 jugadores).
    Solicita los nombres de ambos jugadores, sus elecciones y valida los resultados.
    Luego, guarda los resultados en el archivo 'resultados.log'.
    
    Parámetros de entrada:
        Ninguno.
        
    Parámetros de salida:
        Ninguno.
"""
def juegoMultijugador():
    
    jugadores=[
        {'nombre':'null','eleccion':'null'},
        {'nombre':'null','eleccion':'null'},
        ]
    for jugador in jugadores:
            #Se llama la función para pedir el nombre del jugador
            jugador['nombre']=solicitarNombre()
    partidas=0
    while partidas<=0:
        try:
            partidas=int(input('Ingrese el número de partidas que quiere jugar mayor a 0: '))
        except:
            print('Solo se permiten numeros.')
            partidas=int(input('Ingrese el número de partidas que quiere jugar mayor a 0: '))
    for partida in range(partidas):
        print(f'Partida: {partida+1}')
        for jugador in jugadores:
            #Se llama la función para que el jugador seleccione entre PPT por cada jugador
            seleccionarPPT(jugador,hide=True)

        #Se validan los resultados
        validarResultados(jugadores)

"""
    Función que solicita y valida la elección de Piedra, Papel o Tijera de un jugador.
    Puede ocultar la entrada del usuario si se juega en modo multijugador.
    
    Parámetros de entrada:
        - jugador (dict): Diccionario que contiene el nombre y la elección del jugador.
        - hide (bool): Si es True, oculta la entrada del usuario (útil para multijugador).
                      Por defecto es False.
        
    Parámetros de salida:
        Ninguno.
"""
def seleccionarPPT(jugador,hide=False):
     # Inicio la variable de la expresion regular para validar las 3 opciones
    expresionRegular = r"^Piedra$|^Papel$|^Tijera$"
    eleccion='null'
    # Mientras la opcion no sea valido sigo solicitando
    while not re.findall(expresionRegular, eleccion):
        if hide:
            eleccion=getpass.getpass(f'{jugador["nombre"]}: Escriba alguna de las opciones Piedra/Papel/Tijera: ').capitalize()
        else:
            # Solicito que el usuario ingrese una de las 3 opciones y le pongo la primera letra en May y lo guardo en la variable global eleccion
            eleccion = input(f'{jugador["nombre"]}: Escriba alguna de las opciones Piedra/Papel/Tijera: ').capitalize()
        # Si no es valido se muestra el mensaje de opción válida
        if not re.findall(expresionRegular, eleccion):
            print(f'{colores.RED}Seleccione una opción válida{colores.END}')
        pass
    jugador["eleccion"]=eleccion

"""
    Función que valida los resultados de una partida y determina al ganador.
    Muestra las elecciones de los jugadores y guarda los resultados en 'resultados.log'.
    
    Parámetros de entrada:
        - jugadores (list): Lista de diccionarios con los nombres y elecciones de los jugadores.
        - mostrarEleccion (bool): Si es True, muestra las elecciones de los jugadores.
        Por defecto es True.
        
    Parámetros de salida:
        Ninguno.
"""
def validarResultados(jugadores,mostrarEleccion=True):
    if mostrarEleccion:
        #Mostrar elecciones
        for jugador in jugadores:
            print(f"{jugador['nombre']} eligió: {jugador['eleccion']}") 
        #Abrir archivo de historial
        archivo=open('./resultados.log','a')
        archivo.write(json.dumps(jugadores))
        archivo.write('\n')
        archivo.close()
    #Valido los resultados
    if jugadores[0]["eleccion"] == jugadores[1]["eleccion"]:
        print(f'Empate entre el jugador {jugadores[0]["nombre"]} y el jugador {jugadores[1]["nombre"]} ambos eligieron {jugadores[1]["eleccion"]} !!')
    else:
        match jugadores[1]["eleccion"]:
            case 'Piedra':
                if jugadores[0]["eleccion"] == 'Papel':
                    print(f'El jugador {jugadores[0]["nombre"]} ganó con {jugadores[0]["eleccion"]} vs {jugadores[1]["eleccion"]} del jugador {jugadores[1]["nombre"]}')
                else:
                    print(f'El jugador {jugadores[1]["nombre"]} ganó con {jugadores[1]["eleccion"]} vs {jugadores[0]["eleccion"]} del jugador {jugadores[0]["nombre"]}')
            case 'Papel':
                if jugadores[0]["eleccion"] == 'Tijera':
                    print(f'El jugador {jugadores[0]["nombre"]} ganó con {jugadores[0]["eleccion"]} vs {jugadores[1]["eleccion"]} del jugador {jugadores[1]["nombre"]}')
                else:
                    print(f'El jugador {jugadores[1]["nombre"]} ganó con {jugadores[1]["eleccion"]} vs {jugadores[0]["eleccion"]} del jugador {jugadores[0]["nombre"]}')
            case 'Tijera':
                if jugadores[0]["eleccion"] == 'Piedra':
                    print(f'El jugador {jugadores[0]["nombre"]} ganó con {jugadores[0]["eleccion"]} vs {jugadores[1]["eleccion"]} del jugador {jugadores[1]["nombre"]}')
                else:
                    print(f'El jugador {jugadores[1]["nombre"]} ganó con {jugadores[1]["eleccion"]} vs {jugadores[0]["eleccion"]} del jugador {jugadores[0]["nombre"]}')
    if mostrarEleccion:                
        pausa()


menuPrincipal()