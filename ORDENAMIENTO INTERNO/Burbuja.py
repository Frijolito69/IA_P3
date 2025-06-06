# Definimos la función para realizar el ordenamiento por burbuja (intercambio)
def bubble_sort(lista):
    # Obtenemos la longitud de la lista
    n = len(lista)

    # Recorremos la lista n veces
    for i in range(n):
        # En cada pasada comparamos elementos vecinos
        for j in range(0, n - 1 - i):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[j] > lista[j + 1]:
                # Intercambio de valores usando desempaquetado de tupla
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Lista de ejemplo para ordenar
numeros = [8, 3, 5, 1, 4]

# Mostramos la lista original
print("Lista original:", numeros)

# Llamamos a la función de ordenamiento
bubble_sort(numeros)

# Mostramos la lista ordenada
print("Lista ordenada:", numeros)
