# Función que ordena una lista usando MergeSort
def merge_sort(lista):
    # Caso base: una lista de 0 o 1 elementos ya está ordenada
    if len(lista) <= 1:
        return lista

    # Dividimos la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Ordenamos recursivamente cada mitad
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    # Mezclamos las dos mitades ordenadas y las devolvemos
    return merge(izquierda_ordenada, derecha_ordenada)

# Función que mezcla dos listas ordenadas en una sola ordenada
def merge(izquierda, derecha):
    resultado = []
    i = 0  # Índice para la lista izquierda
    j = 0  # Índice para la lista derecha

    # Comparamos elementos de ambas listas y agregamos el menor
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Si aún quedan elementos en alguna lista, los agregamos al final
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

# Lista de ejemplo para ordenar
numeros = [8, 3, 5, 1, 4]

# Mostramos la lista original
print("Lista original:", numeros)

# Llamamos a MergeSort y guardamos el resultado
ordenada = merge_sort(numeros)

# Mostramos la lista ordenada
print("Lista ordenada:", ordenada)
