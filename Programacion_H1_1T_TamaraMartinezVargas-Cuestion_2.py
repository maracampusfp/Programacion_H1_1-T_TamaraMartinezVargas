# Se importa el módulo random de Python, que contiene funciones para generar números aleatorios
# que luego utilizaré.
import random

# Inicialización de contadores para las partidas ganadas y perdidas.
partidas_ganadas=0
partidas_perdidas=0

# Bucle que continúa mientras el jugador no haya perdido o ganado 3 partidas.
while partidas_perdidas<3 and partidas_ganadas<3:

    # Se le pide al jugador que elija una opción: 1 para Piedra, 2 para Papel o 3 para Tijera.
    opc_jugador=int(input("Elige: 1-Piedra | 2-Papel | 3-Tijera \n"))

    # Se usa la estructura 'match' para comprobar qué opción ha elegido el jugador
    # y mostrarla en pantalla.
    match opc_jugador:
        case 1:
            print("El jugador ha elegido piedra")
        case 2:
            print("El jugador ha elegido papel")
        case 3:
            print("El jugador ha elegido tijera")
        case _:
            # En caso de que el jugador ingrese un valor incorrecto (diferente a los valores
            # comprendidos entre 1 a 3) se le mostrará ERROR y se volverá a mostrar el menú.
            print("ERROR: Opción incorrecta.")

    # Solo se procede si la opción introducida por el jugador es válida. Es decir, la opción es 1, 2 ó 3.
    if opc_jugador>0 and opc_jugador<4:

        # Se genera una elección aleatoria para la máquina usando "randint" de la librería "random"
        # previamente importada al principio del código, indicandole que lo genere entre el rango
        # 1 y 3 inclusives, para guardar en "opc_maquina" 1 (Piedra), 2 (Papel) o 3 (Tijera) de
        # forma aleatoria.
        opc_maquina=random.randint(1, 3)

        # Nuevamente, recurro a usar la estructura "match" para convertir la opción de la máquina
        # en texto y poder mostrarla en pantalla.
        match opc_maquina:
             case 1:
                maquina="Piedra"
             case 2:
                maquina="Papel"
             case 3:
                maquina="Tijera"

        # Se muestra la elección aleatoria de la máquina.
        print("La máquina ha elegido",maquina)

        # Se comprueba si el jugador y la máquina han elegido la misma opción (EMPATE).
        if opc_jugador == opc_maquina:
            print("Habéis empatado!!")

        # Se comprueba si el jugador ha ganado, al cumplirse alguna de las combinaciones (opc_jugador - opc_maquina)
        # que suponga que el jugador ha ganado: cuando el jugador gana si elige Piedra y la máquina Tijera, o
        # Papel contra Piedra, o Tijera contra Papel.
        elif (opc_jugador == 1 and opc_maquina == 3) or (opc_jugador == 2 and opc_maquina == 1) or (opc_jugador == 3 and opc_maquina == 2):
            print("Has ganado!! :)")
            # Se incrementa el contador de partidas ganadas.
            partidas_ganadas=partidas_ganadas+1
            # Si el jugador ha ganado 3 partidas, se informa y se detiene el juego ya que no vuelve a entrar al bucle
            #debido a que no cumple la condición para repetirse.
            if partidas_ganadas==3:
                print("Ya has ganado 3 partidas.")
        else: # Si no es empate ni victoria del jugador, entonces significa que ha perdido y se muestra en pantalla.
            print("Has perdido!! :(")
            # Se incrementa el contador de partidas perdidas.
            partidas_perdidas = partidas_perdidas + 1
            # Si el jugador ha perdido 3 partidas, se informa y se detiene el juego igual que cuando gana 3 veces.
            if partidas_perdidas==3:
                print("Ya has perdido 3 partidas.")













