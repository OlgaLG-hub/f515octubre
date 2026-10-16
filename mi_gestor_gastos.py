gastos = [] # Creamos una lista vacía para guardar los gastos

print("GESTOR DE GASTOS SEMANALES") # Mostramos el título del programa
print("--------------------------")

while True:   # Creamos un bucle que se repite hasta que escribimos "fin"
    entrada = input(
        "Introduce un gasto en euros "
        "(escribe 'fin' para terminar): "
    ) # Pedimos al usuario que introduzca un gasto.
    # El gasto se guarda como texto en la variable entrada

    if entrada.lower() == "fin":   # Comprobamos si el usuario ha escrito "fin"
        break   # Terminamos el bucle si la respuesta es "fin"

    try:   # Intentamos convertir el texto en un número
        gasto = float(entrada.replace(",", "."))  # Cambiamos la coma por un punto y convertimos el texto en número

        if gasto < 0:  # Comprobamos si el gasto es negativo
            print("El gasto no puede ser negativo.")  # Mostramos un mensaje de error
            continue # Volvemos a pedir otro gasto

        gastos.append(gasto) # Añadimos el gasto a la lista
        print("Gasto guardado correctamente.")
# Confirmamos que el gasto se ha añadido a la lista
    except ValueError: # Detectamos si el usuario ha introducido un valor incorrecto
        print("Introduce un número válido.") # Pedimos que introduzca un número válido

if len(gastos) == 0: # Comprobamos si la lista está vacía
    print("No hay gastos registrados.") # Avisamos de que no hay gastos

else: # Si hay gastos, calculamos los resultados
    total = sum(gastos) # Sumamos todos los gastos
    media = total / len(gastos) # Calculamos la media dividiendo el total entre el número de gastos

    print("\nRESUMEN DE GASTOS") # Mostramos el título del resumen
    print("-----------------")
    print("Lista de gastos:", gastos) # Mostramos todos los gastos introducidos
    print(f"Total de gastos: {total:.2f} €")  # Mostramos el total con dos decimales
    print(f"Gasto medio: {media:.2f} €") # Mostramos la media con dos decimales

    print("\nGastos superiores a 20 €:") # Mostramos el título de los gastos superiores a 20 euros

    encontrados = False # Creamos una variable para saber si encontramos algún gasto mayor de 20

    for gasto in gastos: # Recorremos todos los gastos de la lista
        if gasto > 20: # Comprobamos si el gasto es mayor de 20 euros
            print(f"- {gasto:.2f} €") # Mostramos el gasto si supera los 20 euros
            encontrados = True # Indicamos que hemos encontrado al menos un gasto

    if not encontrados: # Comprobamos si no hemos encontrado ningún gasto mayor de 20
        print("No hay gastos superiores a 20 €.")

    presupuesto = 100 # Establecemos el presupuesto semanal en 100 euros

    print("\nPRESUPUESTO SEMANAL")
    print("-------------------")

    if total > presupuesto: # Comprobamos si los gastos superan los 100 euros
        print("Has superado el presupuesto semanal de 100 €.")
    else: # Si los gastos no superan los 100 euros...
        print("No has superado el presupuesto semanal de 100 €.")

    restante = presupuesto - total # Calculamos el dinero que queda del presupuesto

    print(f"Presupuesto: {presupuesto:.2f} €") # Mostramos el presupuesto semanal
    print(f"Dinero restante: {restante:.2f} €") # Mostramos el dinero restante o el exceso de gasto
