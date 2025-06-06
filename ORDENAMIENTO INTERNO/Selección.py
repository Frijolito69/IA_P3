# Definimos la función que realizará el ordenamiento por selección
def selection_sort(lista):
    # Recorremos toda la lista
    for i in range(len(lista)):
        # Suponemos que el elemento actual es el mínimo
        indice_minimo = i

        # Recorremos el resto de la lista para encontrar si hay un valor menor
        for j in range(i + 1, len(lista)):
            # Si encontramos un elemento menor, actualizamos el índice mínimo
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Si encontramos un nuevo mínimo, lo intercambiamos con el actual
        if indice_minimo != i:
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

# Lista de ejemplo para ordenar
numeros = [8, 3, 5, 1, 4]

# Mostramos la lista original
print("Lista original:", numeros)

# Llamamos a la función para ordenar la lista
selection_sort(numeros)

# Mostramos la lista ordenada
print("Lista ordenada:", numeros)
