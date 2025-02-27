from Metodos import llenar_matriz, imprimir_matriz

def ejecutar_punto4():
    print("\n--- Ejercicio 4: Sumar columnas y encontrar la columna con la máxima suma ---")
    
    filas, columnas = 10, 10
    matriz = llenar_matriz(filas, columnas, 1, 50)  # Números aleatorios entre 1 y 50
    imprimir_matriz(matriz)
    
    # Calcular la suma de cada columna
    suma_columnas = [sum(matriz[f][c] for f in range(filas)) for c in range(columnas)]
    
    # Determinar la columna con la máxima suma
    max_suma = max(suma_columnas)
    columna_max = suma_columnas.index(max_suma)
    
    print(f"\n📈 La columna con la máxima suma es la columna {columna_max} con una suma de {max_suma}.")
    print(f"📊 Sumas de todas las columnas: {suma_columnas}")
