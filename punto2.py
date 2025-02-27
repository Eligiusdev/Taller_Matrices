from Metodos import llenar_matriz, imprimir_matriz

def ejecutar_punto2():
    print("\n--- Ejercicio 2: Encontrar la posición del número mayor en una matriz 5x5 ---")
    
    filas, columnas = 5, 5
    matriz = llenar_matriz(filas, columnas, 1, 100)  # Números aleatorios diferentes entre 1 y 100
    imprimir_matriz(matriz)
    
    max_valor = None
    posicion_max = (-1, -1)
    
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if max_valor is None or valor > max_valor:
                max_valor = valor
                posicion_max = (i, j)
    
    print(f"\n💎 El número mayor es {max_valor}, en la posición [fila, columna]: {posicion_max}")
