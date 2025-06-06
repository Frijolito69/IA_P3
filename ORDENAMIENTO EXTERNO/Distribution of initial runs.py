# Simula la lectura y distribución de runs
def distribuir_corridas_iniciales(lista, tam_bloque):
    corridas = []

    # Recorremos la lista de 'tam_bloque' en 'tam_bloque'
    for i in range(0, len(lista), tam_bloque):
        bloque = lista[i:i + tam_bloque]  # Extraemos el bloque
        bloque.sort()  # Lo ordenamos en memoria
        corridas.append(bloque)  # Lo almacenamos como run

    return corridas

# Lista grande a ordenar (simulación de un archivo)
datos = [9, 3, 7, 1, 5, 8, 2, 4, 6, 0]

# Tamaño máximo que cabe en memoria (simulado)
tam_bloque = 4

# Distribuimos las corridas iniciales
corridas_iniciales = distribuir_corridas_iniciales(datos, tam_bloque)

# Mostramos el resultado
print("Corridas iniciales distribuidas:")
for i, corrida in enumerate(corridas_iniciales):
    print(f"Run {i + 1}:", corrida)
