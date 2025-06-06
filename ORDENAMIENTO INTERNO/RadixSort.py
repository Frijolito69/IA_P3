# Función que obtiene el dígito en cierta posición (0 = unidades, 1 = decenas, etc.)
def obtener_digito(numero, posicion):
    return (numero // (10 ** posicion)) % 10

# Función que obtiene la cantidad de dígitos de un número
def contar_digitos(numero):
    return len(str(numero))

# Función principal de Radix Sort
def radix_sort(lista):
    # Encontramos el número con más dígitos
    max_digitos = max(contar_digitos(num) for num in lista)

    # Recorremos cada posición de los dígitos (de derecha a izquierda)
    for posicion in range(max_digitos):
        # Creamos 10 cubetas (0 al 9) para cada posible dígito
        cubetas = [[] for _ in range(10)]

        # Colocamos cada número en la cubeta según el dígito actual
        for numero in lista:
            digito = obtener_digito(numero, posicion)
            cubetas[digito].append(numero)

        # Aplanamos las cubetas y actualizamos la lista
        lista.clear()
        for cubeta in cubetas:
            lista.extend(cubeta)

# Lista de ejemplo
numeros = [170, 45, 75, 90, 802, 24, 2, 66]

# Mostramos la lista original
print("Lista original:", numeros)

# Aplicamos Radix Sort
radix_sort(numeros)

# Mostramos la lista ordenada
print("Lista ordenada:", numeros)
