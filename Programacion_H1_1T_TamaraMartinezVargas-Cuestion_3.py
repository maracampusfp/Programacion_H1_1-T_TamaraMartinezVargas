# Inicialización de variables
saldo=0 # Almacenará el saldo de la cuenta
saldo_inicial=-1 # Inicialización con valor negativo para forzar la validación necesaria más adelante

cont_ingresos=0 # Contador de ingresos realizados
cont_retiradas=0 # Contador de retiradas realizadas

# Bucle para pedir el saldo inicial hasta que se introduzca un valor positivo
while saldo_inicial<0:

    # Se solicita el saldo inicial, que puede ser decimal, como exige el hito.
    saldo_inicial = float(input("Introduce saldo inicial de la cuenta: "))

    # Si el saldo es negativo, se muestra un mensaje de error
    if saldo_inicial<0:
        print("ERROR: El saldo introducido es negativo. Debe ser positivo.")

# Se actualiza el saldo con el saldo inicial valido introducido
saldo=saldo+saldo_inicial

# Se muestra el saldo inicial con dos decimales, utilizando "%2f"%variable
print("%.2f"%saldo,"€")

# Bucle principal que muestra un menú de opciones hasta que el usuario elija 5-salir (opc=5)
# Se inicializa opc con un valor distinto a 5 para entrar en el bucle while
opc=1
while opc!=5:

    # Se muestra el menú con las opciones
    print("Menú")
    print("1. Ingresar dinero.")
    print("2. Retirar dinero.")
    print("3. Mostrar saldo.")
    print("4. Estadísticas.")
    print("5. Salir.")

    # Se solicita al usuario que elija una opción
    opc = int(input("Elige una opción:"))

    # Se comprueba la opción introducida por el usuario usando la estructura 'match'
    match opc:

        # Opción 1: Ingresar dinero
        case 1:
            print("*** INGRESAR DINERO ***")

            # Se solicita la cantidad a ingresar, que puede ser decimal
            ingreso=float(input("Introduce cantidad a ingresar: "))

            # Si el ingreso es negativo, se muestra un mensaje de error
            if ingreso<0:
                print("OPERACIÓN DENEGADA: LA CANTIDAD DEBE SER POSITIVA.")
            else:

                # Si es positivo, se actualiza el saldo
                saldo=saldo+ingreso
                # se muestra un mensaje en pantalla verificando al usuario la acción realizada
                print("Se ha añadido","%.2f"%ingreso,"€ a su cuenta.")
                # se incrementa el contador de ingresos
                cont_ingresos=cont_ingresos+1
        case 2:
            # Opción 2: Retirar dinero
            print("*** RETIRAR DINERO ***")

            # Se solicita la cantidad a retirar
            retirar = float(input("Introduce cantidad a retirar: "))

            #Si la cantidad introducida es negativa se muestra un mensaje de error.
            if retirar<0:
                print("OPERACIÓN DENEGADA: LA CANTIDAD DEBE SER POSITIVA.")
            else:

                # Si el saldo disponible es insuficiente para poder realizar la retirada
                # indicada, se muestra un error.
                if saldo-retirar<0:
                    print("OPERACIÓN DENEGADA: SALDO INSUFICIENTE.")
                    print("La cantidad que desea retirar es mayor al saldo disponible.")
                else:

                    # Si el saldo es suficiente, se actualiza el saldo
                    saldo=saldo-retirar
                    # Se muestra un mensaje en pantalla verificando al usuario la acción realizada
                    print("Se ha retirado", "%.2f" % retirar, "€ de su cuenta.")
                    # Se incrementa el contador de retiradas
                    cont_retiradas=cont_retiradas+1
        case 3:
            # Opción 3: Mostrar saldo
            print("*** SALDO ACTUAL EN LA CUENTA ***")
            # Se muestra el saldo actual con dos decimales
            print("El saldo actual es: ","%.2f"%saldo,"€")

        case 4:
            # Opción 4: Mostrar estadísticas
            print("*** ESTADÍSTICAS ***") #cuantos ingresos y retiradas se han efectuado
            # Muestra el número de ingresos y retiradas realizados hasta el momento
            print("Se han realizado ",cont_ingresos," ingresos.")
            print("Se han realizado ",cont_retiradas," retiradas.")

        case 5:
            # Opción 5: Salir del programa
            print("Has elegido salir.")

        case _:
            # Si el usuario introduce una opción no válida, se muestra un mensaje de error
            print("ERROR: Opción introducida incorrecta.")