# Función que mezcla dos sublistas ordenadas
def mezclar(lista1, lista2):
    resultado = []
    i = j = 0

    # Comparamos y agregamos el menor elemento
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregamos los elementos restantes de ambas listas
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

# Función principal de mezcla directa
def mezcla_directa(lista):
    n = len(lista)
    paso = 1  # Tamaño inicial de los bloques a mezclar

    while paso < n:
        nuevo = []  # Lista temporal para almacenar el resultado

        for i in range(0, n, 2 * paso):
            # Obtenemos dos bloques de longitud 'paso'
            bloque1 = lista[i:i + paso]
            bloque2 = lista[i + paso:i + 2 * paso]

            # Mezclamos los bloques y los agregamos al nuevo resultado
            nuevo.extend(mezclar(bloque1, bloque2))

        lista = nuevo  # Reemplazamos la lista original
        paso *= 2  # Duplicamos el tamaño de los bloques

    return lista

# Lista de ejemplo
numeros = [8, 3, 5, 1, 4, 7, 2, 6]

# Mostramos la lista original
print("Lista original:", numeros)

# Aplicamos mezcla directa
ordenada = mezcla_directa(numeros)

# Mostramos la lista ordenada
print("Lista ordenada:", ordenada)
