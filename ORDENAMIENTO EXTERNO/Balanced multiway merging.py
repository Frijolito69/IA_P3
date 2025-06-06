import heapq

# Función que mezcla múltiples listas ordenadas usando un heap (montículo)
def mezcla_multiway(listas):
    resultado = []
    heap = []

    # Insertamos el primer elemento de cada lista en el heap junto con el índice de la lista y del elemento
    for i, lista in enumerate(listas):
        if lista:
            heapq.heappush(heap, (lista[0], i, 0))

    # Mientras haya elementos en el heap
    while heap:
        valor, lista_indice, elemento_indice = heapq.heappop(heap)
        resultado.append(valor)

        # Si la lista tiene más elementos, insertamos el siguiente
        if elemento_indice + 1 < len(listas[lista_indice]):
            siguiente = listas[lista_indice][elemento_indice + 1]
            heapq.heappush(heap, (siguiente, lista_indice, elemento_indice + 1))

    return resultado

# Simulamos sublistas ordenadas
sublistas = [
    [1, 4, 7],
    [2, 5, 8],
    [0, 3, 6],
]

# Mostramos las sublistas originales
print("Sublistas:", sublistas)

# Mezclamos todas las sublistas en una sola ordenada
ordenada = mezcla_multiway(sublistas)

# Mostramos el resultado ordenado
print("Lista mezclada:", ordenada)
