# Aprendizaje-Autónomo-2
Este repo es para el trabajo de Aprendizaje autónomo 2 de la materia LOGICA DE PROGRAMACION 2-ECC-1D. En el se pueden encontrar los diagramas y el codigo para el juego de Piedra Papel y Tijeras en python.

## Documentación
En la carpeta Diagramas se encuentran los diagramas del juego.
### Diagrama general del Juego
![](<Diagramas/Diagrama del juego.png>)

```
@startuml
!theme bluegray

start

:Importar modulos (re, random); 

repeat
  :Solicitar entrada del jugador; <<input>>
  :Convertir primera letra en mayúscula; 
  if (Entrada válida?  \n'Piedra|Papel|Tijera') then (no)
    :Mostrar "Seleccione una opción válida"; <<output>>
  endif
repeat while (Entrada válida?  \n'Piedra|Papel|Tijera') is (no) not (si)

:Seleccionar elección aleatoria del sistema;
:Mostrar "Eleccción del sistema " ;<<output>>
:Validacion de resultado;
note right
 Este paso contiene su propio diagrama
end note


stop

@enduml

```


### Diagrama del paso de validacion de datos
![](<Diagramas/Diagrama Validacion de resultados.png>)

```
@startuml
!theme bluegray

start
note right
 Diagrama de validacion de datos
end note


if (Elección del jugador == Elección del sistema?) then (sí)
  :Mostrar "Empate"; <<output>>
else (no)
 switch (Elección del sistema?)
 case (Piedra)
  if (Elección del jugador == Papel?) then (si)
      :Mostrar "Ganador: Jugador"; <<output>>
    else (no)
      :Mostrar "Ganador: Sistema"; <<output>>
    endif
 case (Papel) 
 if (Elección del jugador == Tijera?) then (si)
        :Mostrar "Ganador: Jugador"; <<output>>
      else (no)
        :Mostrar "Ganador: Sistema"; <<output>>
      endif
 case (Tijera)
  if (Elección del jugador == Piedra?) then (si)
        :Mostrar "Ganador: Jugador";<<output>>
      else (no)
        :Mostrar "Ganador: Sistema"; <<output>>
      endif
 endswitch 
endif
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