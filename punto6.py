from Metodos import llenar_matriz, imprimir_matriz

def ejecutar_punto6():
    print("\n--- Ejercicio 6: Almacenar la suma de filas y columnas en un vector ---")
    
    filas, columnas = 8, 8
    matriz = llenar_matriz(filas, columnas, 1, 50)  # Números aleatorios entre 1 y 50
    imprimir_matriz(matriz)
    
    # Calcular la suma de cada fila y almacenarla en un vector
    suma_filas = [sum(fila) for fila in matriz]
    
    # Calcular la suma de cada columna y almacenarla en un vector
    suma_columnas = [sum(matriz[f][c] for f in range(filas)) for c in range(columnas)]
    
    # Unir ambos vectores en un solo resultado
    vector_resultante = suma_filas + suma_columnas
    
    print(f"\n📦 Vector resultante (Suma de filas + Suma de columnas): {vector_resultante}")
