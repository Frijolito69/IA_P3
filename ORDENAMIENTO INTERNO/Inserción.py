# Definimos la función que realizará el ordenamiento por inserción
def insertion_sort(lista):
    # Recorremos la lista desde el segundo elemento (índice 1) hasta el final
    for i in range(1, len(lista)):
        # Guardamos el valor actual que queremos insertar en la parte ordenada
        actual = lista[i]
        # Creamos una variable j que apunta al índice anterior al actual
        j = i - 1

        # Mientras j no sea menor que 0 y el elemento en lista[j] sea mayor que el actual
        while j >= 0 and lista[j] > actual:
            # Movemos el elemento lista[j] una posición a la derecha
            lista[j + 1] = lista[j]
            # Disminuimos j para comparar con el siguiente elemento a la izquierda
            j -= 1

        # Cuando encontramos la posición correcta, insertamos el valor actual
        lista[j + 1] = actual

# Lista de ejemplo que se ordenará
numeros = [8, 3, 5, 1, 4]

# Mostramos la lista antes de ordenarla
print("Lista original:", numeros)

# Llamamos a la función para ordenar la lista
insertion_sort(numeros)

# Mostramos la lista ya ordenada
print("Lista ordenada:", numeros)