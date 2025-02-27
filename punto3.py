from Metodos import llenar_matriz, imprimir_matriz

def ejecutar_punto3():
    print("\n--- Ejercicio 3: Suma de filas y columnas en una matriz 5x5 ---")
    
    filas, columnas = 5, 5
    matriz = llenar_matriz(filas, columnas, 1, 50)  # Números aleatorios entre 1 y 50
    imprimir_matriz(matriz)
    
    # Calcular la suma de cada fila y almacenarla en un vector
    suma_filas = [sum(fila) for fila in matriz]
    
    # Calcular la suma de cada columna y almacenarla en un vector
    suma_columnas = [sum(matriz[f][c] for f in range(filas)) for c in range(columnas)]
    
    print(f"\n📊 Vector de la suma de cada fila: {suma_filas}")
    print(f"📈 Vector de la suma de cada columna: {suma_columnas}")
