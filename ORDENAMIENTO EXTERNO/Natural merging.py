# Función que mezcla dos sublistas ordenadas
def mezclar(lista1, lista2):
    resultado = []
    i = j = 0

    # Compara elementos de ambas listas y agrega el menor
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agrega los elementos restantes de ambas listas
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

# Función principal de mezcla natural
def mezcla_natural(lista):
    n = len(lista)

    while True:
        i = 0
        nuevas_listas = []

        # Detectamos sublistas ya ordenadas (naturales)
        while i < n:
            sublista = [lista[i]]
            i += 1

            # Agrupamos mientras esté ordenado
            while i < n and lista[i] >= sublista[-1]:
                sublista.append(lista[i])
                i += 1

            nuevas_listas.append(sublista)

        # Si solo queda una sublista, ya está ordenada
        if len(nuevas_listas) == 1:
            return nuevas_listas[0]

        # Mezclamos las sublistas de dos en dos
        lista = []
        for j in range(0, len(nuevas_listas), 2):
            if j + 1 < len(nuevas_listas):
                mezclada = mezclar(nuevas_listas[j], nuevas_listas[j + 1])
                lista.extend(mezclada)
            else:
                lista.extend(nuevas_listas[j])
# Lista desordenada
numeros = [2, 4, 6, 1, 3, 5, 7, 0]

print("Lista original:", numeros)

# Aplicamos mezcla natural
ordenada = mezcla_natural(numeros)

print("Lista ordenada:", ordenada)
