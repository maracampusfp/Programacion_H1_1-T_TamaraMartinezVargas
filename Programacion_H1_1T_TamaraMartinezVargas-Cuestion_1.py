# La variable opc se usará para guardar la opción del menú elegida por el usuario.
# Se inicializa en 1 para asegurar que el bucle while posterior se ejecute al menos una vez,
# ya que opc=3 implica salir del programa.
opc=1

# Este bucle while se ejecutará mientras la opción elegida por el usuario sea distinta de 3
# (es decir, mientras no elija "Salir").
while opc!=3:

    # Se muestra el menú con tres opciones.
    print("\nMENÚ")
    print("1.- Cuadrado.")
    print("2.- Rectángulo.")
    print("3.- Salir.")

    # Se solicita al usuario que elija una opción, y se guarda el valor en la variable opc.
    opc = int (input("Dime una opción: "))

    # Se usa la estructura match para realizar diferentes acciones según el valor de la variable opc.
    match opc:

        # Caso 1 (CUADRADO): El usuario ha elegido dibujar un cuadrado.
        case 1:

            # Se pide al usuario el tamaño del lado del cuadrado.
            lado=int(input("\nDime el lado del cuadrado: "))

            # Se comprueba que el valor introducido sea positivo, ya que no tendría sentido
            # un lado negativo o cero.
            if lado<=0:

                # Si el lado es menor o igual a cero, se muestra un mensaje de error.
                print("ERROR: La medida es incorrecta. Debe ser positiva (mayor que cero).")
            else:
                print("")

                # Si la medida introducida (lado) es correcta, se procede a dibujar el cuadrado.
                # Se hace a través de dos bucles for anidados para generar las filas y columnas
                # de asteriscos.
                for i in range(1,lado+1):

                    # Este bucle imprime una fila de asteriscos.
                    for i in range(1,lado+1):

                        # Se imprime en pantalla un asterisco (*) sin salto de línea, para lo cual
                        # se ha usado end="", puesto que por defecto print, por defecto, realiza un
                        # salto de linea. [print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)]
                        print(end="*")

                    # Al terminar la fila, se añade un salto de línea para pasar a la siguiente.
                    print("")

                # Una vez dibujado el cuadrado, se muestra el área (lado^2 o lado*lado).
                print("\nSu área es ",lado**2)

                # También se muestra el perímetro (lado*4, ya que todos los lados de un cuadrado son iguales).
                print("Su perímetro es ",lado*4)

        # Caso 2(RECTÁNGULO): El usuario ha elegido dibujar un rectángulo.
        case 2:

            # Se pide al usuario las medidas del rectángulo: base y altura.
            base = int(input("\nDime la base del rectángulo: "))
            altura = int(input("Dime la altura del rectángulo: "))

            # Se comprueba que ambos valores sean positivos, ya que la base o la altura no pueden ser
            # cero o negativas. No tendría sentido, al igual que en el cuadrado o cualquier figura.
            if base<=0 or altura<=0:

                # Si alguna de las dos medidas es inválida, se muestra un mensaje de error al usuario.
                print("ERROR: Ambas medidas deben ser positivas (mayor que cero).")
            else:
                print("")

                # Si las medidas son correctas, se procede a "dibujar" el rectángulo.
                # De nuevo, se recurre al uso de dos bucles for anidados, similar al cuadrado,
                # pero esta vez las filas y columnas dependen de la base y la altura.
                for i in range(1,altura+1):

                    # El bucle interno imprime una fila de asteriscos con longitud igual a la base.
                    for i in range(1,base+1):

                        # Se imprime un asterisco (*) sin salto de línea. De nuevo usando end="".
                        print(end="*")

                        # Al terminar la fila, añadimos un salto de línea para pasar a la siguiente.
                    print("")

                # Una vez mostrado en pantalla el rectángulo con asteriscos, se muestra
                # el área (base * altura).
                print("\nSu área es ",base*altura)

                # También se muestra el perímetro (2 * (base + altura)).
                print("Su perímetro es ",base*2+altura*2)

        # Caso 3 (SALIR): El usuario ha elegido salir del programa.
        case 3:

            # Mostramos un mensaje de despedida.
            print("\nHas elegido salir del programa.")

        # En cualquier otro caso diferente a los anteriores: Si el usuario introduce una opción
        # no válida (distinta de 1, 2 o 3).
        case _:

            # Mostramos un mensaje de error indicando que la opción es incorrecta.
            print("\nERROR: La opción elegida no es correcta.")