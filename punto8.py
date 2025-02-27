from Metodos import llenar_matriz, imprimir_matriz

def ejecutar_punto8():
    print("\n--- Ejercicio 8: Fila con la mayor suma ---")
    
    filas, columnas = 5, 5
    matriz = llenar_matriz(filas, columnas, 1, 50)  # Números aleatorios entre 1 y 50
    imprimir_matriz(matriz)
    
    # Calcular la suma de cada fila
    suma_filas = [sum(fila) for fila in matriz]
    
    # Determinar la fila con la mayor suma
    max_suma = max(suma_filas)
    fila_max = suma_filas.index(max_suma)
    
    print(f"\n📈 La fila con la mayor suma es la fila {fila_max}, con una suma de {max_suma}.")
    print(f"📊 Sumas de todas las filas: {suma_filas}")
