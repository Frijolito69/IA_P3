# Definimos la función QuickSort
def quicksort(lista):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # Elegimos un pivote (por simplicidad, el primer elemento)
    pivote = lista[0]

    # Creamos listas para los menores y mayores al pivote
    menores = []
    mayores = []

    # Recorremos los elementos (excepto el pivote)
    for i in range(1, len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])  # Menores al pivote
        else:
            mayores.append(lista[i])  # Mayores o iguales

    # Aplicamos QuickSort a las listas menores y mayores (recursión)
    return quicksort(menores) + [pivote] + quicksort(mayores)

# Lista de ejemplo
numeros = [8, 3, 5, 1, 4]

# Mostramos la lista original
print("Lista original:", numeros)

# Ordenamos la lista con QuickSort y guardamos el resultado
ordenada = quicksort(numeros)

# Mostramos la lista ordenada
print("Lista ordenada:", ordenada)
