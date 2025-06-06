# Definimos la clase Nodo para el árbol binario
class Nodo:
    def __init__(self, valor):
        # Valor almacenado en el nodo
        self.valor = valor
        # Subárbol izquierdo (menores)
        self.izquierda = None
        # Subárbol derecho (mayores o iguales)
        self.derecha = None

# Función para insertar un nuevo valor en el árbol
def insertar(nodo, valor):
    # Si el árbol está vacío, creamos un nuevo nodo
    if nodo is None:
        return Nodo(valor)
    
    # Si el valor es menor, insertamos a la izquierda
    if valor < nodo.valor:
        nodo.izquierda = insertar(nodo.izquierda, valor)
    # Si el valor es mayor o igual, insertamos a la derecha
    else:
        nodo.derecha = insertar(nodo.derecha, valor)

    return nodo

# Función para recorrer el árbol en inorden y llenar una lista
def recorrido_inorden(nodo, resultado):
    if nodo is not None:
        # Recorremos el subárbol izquierdo
        recorrido_inorden(nodo.izquierda, resultado)
        # Agregamos el valor del nodo actual
        resultado.append(nodo.valor)
        # Recorremos el subárbol derecho
        recorrido_inorden(nodo.derecha, resultado)

# Función principal de ordenamiento usando árbol
def tree_sort(lista):
    raiz = None  # Árbol vacío al inicio

    # Insertamos todos los elementos en el árbol
    for valor in lista:
        raiz = insertar(raiz, valor)

    resultado = []
    # Recorremos el árbol para obtener la lista ordenada
    recorrido_inorden(raiz, resultado)
    
    # Copiamos el resultado ordenado de vuelta a la lista original
    for i in range(len(lista)):
        lista[i] = resultado[i]

# Lista de ejemplo
numeros = [8, 3, 5, 1, 4]

# Mostramos la lista original
print("Lista original:", numeros)

# Llamamos a la función de ordenamiento por árbol
tree_sort(numeros)

# Mostramos la lista ordenada
print("Lista ordenada:", numeros)
