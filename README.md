# Aprendizaje-Autónomo-2

Este repo es para el trabajo de Aprendizaje Autónomo 2 de la materia LÓGICA DE PROGRAMACIÓN 2-ECC-1D. En él se pueden encontrar los diagramas y el código para el juego de Piedra, Papel y Tijeras en Python.

## Descripción del juego
Piedra, Papel y Tijera es un juego clásico y sencillo que se juega entre dos participantes (un jugador contra otro o un jugador contra la computadora). El objetivo es elegir una de las tres opciones: Piedra, Papel o Tijera.

## Reglas básicas

**Objetivo:** El objetivo del juego es vencer a tu oponente eligiendo la opción que supera a la suya.

**Opciones:**
- **Piedra:** Representada por un puño cerrado.
- **Papel:** Representado por la mano extendida, con la palma hacia abajo o hacia arriba.
- **Tijera:** Representada por los dedos índice y medio extendidos, formando una 'V'.

**Relaciones de fuerza:**
- La piedra aplasta la tijera (la piedra gana a la tijera).
- La tijera corta el papel (la tijera gana al papel).
- El papel envuelve la piedra (el papel gana a la piedra).
- **Empate:** Si ambos jugadores eligen la misma opción, la ronda termina en empate y se vuelve a jugar.

---

### Modo contra la computadora
- El jugador elige una de las tres opciones: piedra, papel o tijera.
- La computadora elige una opción al azar.
- Se comparan las opciones según las relaciones de fuerza mencionadas anteriormente.
- Se determina el ganador de la ronda (jugador, computadora o empate).
- Se pueden jugar varias rondas para determinar un ganador final.

---

### Modo Multijugador (2 jugadores)
- Dos jugadores se enfrentan.
- Ambos jugadores eligen una de las tres opciones: piedra, papel o tijera.
- Se comparan las opciones según las relaciones de fuerza.
- Se determina el ganador de la ronda (jugador 1, jugador 2 o empate).
- Se pueden jugar varias rondas para determinar un ganador final.

## Detalles del proyecto
- **IDE:** Este proyecto fue desarrollad y probado en VSCode integrado con Github para poder administrar los cambios en el repositorio.
- **Lenguaje de programación:** Para este proyecto se utilizo Python V3.10

## Librerías
- re: Utilizada para validar expresiones regulares
- random: Utilizada en la selección de aleatoria del sistema
- json: Utilizada en las estadísticas e historial de versiones
- getpass: Utilizada en el juego multijugador para que no se vea lo que se escribe


## Estructura
En la carpeta Diagramas se encuentran los diagramas del juego.

### Diagrama general del Juego
![](<Diagramas/Diagrama del juego v3.png>)

```
@startuml
!theme bluegray
start

repeat
  :Menú Principal;
  switch (Opción seleccionada?)
  case (Reglas)
    :Reglas;
  case (Contra la computadora)
    :Menú Juego Contra Sistema;
    switch (Opción seleccionada?)
    case (Ver Reglas)
      :Reglas;
    case (Jugar Contra la computadora)
      :Juego ContraSistema;
    case (Ver estadísticas)
      :Menú Estadisticas;
    case (Regresar al menú principal)
      :Menú Principal;
    endswitch
  case (Multijugador (2 jugadores))
    :Menú Juego Multijugador;
  case (Ver estadísticas)
    :Menú Estadisticas;
    switch (Opción seleccionada?)
    case (Ver estadísticas)
      :Estadisticas;
    case (Ver Historial)
      :Historial;
    case (Limpiar estadísticas)
      :Limpia resultados.log;
    case (Regresar al menú principal)
      :Menú Principal;
    endswitch
  endswitch
repeat while (¿Continuar?) is (Sí)
stop
@enduml
```

### Diagrama del paso de validación de resultados
![](<Diagramas/validarResultados.png>)

```
@startuml
!theme bluegray
start

if (mostrar Eleccion?) then (Sí)
  :Mostrar elecciones de los jugadores;
  :Guardar resultados en resultados.log;
endif

if (elección jugador 1 == elección jugador 2?) then (Sí)
  :Mostrar "Empate";
else (No)
  :Validar resultados;
endif

stop
@enduml
```


### Diagrama del paso de validación de resultados
![](<Diagramas/Diagrama Validacion de resultados.png>)

```
@startuml
!theme bluegray
start

if (mostrar Eleccion?) then (Sí)
  :Mostrar elecciones de los jugadores;
  :Guardar resultados en resultados.log;
endif

if (elección jugador 1 == elección jugador 2?) then (Sí)
  :Mostrar "Empate";
else (No)
  :Validar resultados;
endif

stop
@enduml
```

### Diagrama de función de selección entre Piedra, Papel y Tijera
![](<Diagramas/seleccionarPPT.png>)

```
@startuml
!theme bluegray
start

if (hide?) then (Sí)
  :Ocultar entrada (usar getpass);
else (No)
  :Mostrar entrada normal;
endif

repeat
  :Solicitar elección (Piedra, Papel, Tijera);
  if (elección válida?) then (Sí)
    :Asignar elección al jugador;
    break;
  else (No)
    :Mostrar "Opción inválida";
  endif
repeat while (elección válida?) is (No)

stop
@enduml
```

### Diagrama de la lógica de juego multijugador
![](<Diagramas/juegoMultijugador.png>)

```
@startuml
!theme bluegray
start

:Solicitar nombre del Jugador 1;
:Solicitar elección del Jugador 1 (seleccionarPPT);
:Solicitar nombre del Jugador 2;
:Solicitar elección del Jugador 2 (seleccionarPPT);
:Validar resultados;

stop
@enduml
```

### Diagrama de la lógica de juego contra el Sistema
![](<Diagramas/juegoContraSistema.png>)

```
@startuml
!theme bluegray
start

:Solicitar nombre del Jugador;

:Solicitar elección del Jugador (seleccionarPPT);
:Generar elección aleatoria del Sistema;

:Validar resultados (validarResultados);

stop
@enduml
```

### Diagrama de la lógica de validación y solicitud de nombres
![](<Diagramas/solicitarNombre.png>)

```
@startuml
!theme bluegray
start

repeat
  :Solicitar nombre del jugador;
  if (nombre válido?) then (Sí)
    :Retornar nombre;
    break;
  else (No)
    :Mostrar "Nombre inválido";
  endif
repeat while (nombre válido?) is (No)

stop
@enduml
```

### Diagrama de la lógica de historial de partidas
![](<Diagramas/historial.png>)

```
@startuml
!theme bluegray
start

:Abrir archivo resultados.log;

repeat
  :Leer línea del archivo;
  if (línea válida?) then (Sí)
    :Mostrar resultado de la partida;
  else (No)
    break;
  endif
repeat while (hay más líneas?) is (Sí)

:Cerrar archivo;

stop
@enduml
```

### Diagrama de la lógica de estadísticas
![](<Diagramas/estadisticas.png>)


```
@startuml
!theme bluegray
start

:Abrir archivo resultados.log;

:Inicializar contadores de estadísticas;

repeat
  :Leer línea del archivo;
  if (línea válida?) then (Sí)
    :Procesar resultado de la partida;
    :Actualizar estadísticas;
  else (No)
    break;
  endif
repeat while (hay más líneas?) is (Sí)

:Mostrar estadísticas finales;
:Cerrar archivo;

stop
@enduml
```

### Diagrama de la lógica que administra las entradas de los menús
![](<Diagramas/entradasDelMenu.png>)


```
@startuml
!theme bluegray
start

repeat
  :Solicitar entrada del usuario;
  if (entrada es número válido?) then (Sí)
    if (entrada está en rango de opciones?) then (Sí)
      :Retornar opción seleccionada;
      break;
    else (No)
      :Mostrar "Opción fuera de rango";
    endif
  else (No)
    :Mostrar "Entrada inválida";
  endif
repeat while (entrada válida?) is (No)

stop
@enduml
```


### Diagrama de Arquitectura
![](<Diagramas/Diagrama de arquitectura.png>)


```
@startuml
node "Sistema Operativo (Windows,Linux,Mac)" {
    node "Python 3"{
      node "Juego de Piedra, Papel o Tijera" {
        [Python 3] --> [Sistema del juego]
        [Sistema del juego] --> [Lógica del Juego] 
        node "Lógica del Juego" {
         [Lógica del Juego] --> [Entrada del Jugador]
         [Lógica del Juego] --> [Generador Aleatorio]
         [Lógica del Juego] --> [Validador de resultado]
        }
      }
    }
    
}
node "Entrada/Salida" {
    [Entrada del Jugador] --> [Teclado]
    [Resultado] --> [Pantalla]
}
@enduml
```