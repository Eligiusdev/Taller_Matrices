from Metodos import llenar_matriz, imprimir_matriz

def ejecutar_punto9():
    print("\n--- Ejercicio 9: Operaciones con máximo y mínimo en una matriz ---")
    
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    
    matriz = llenar_matriz(filas, columnas, 1, 100)  # Números aleatorios entre 1 y 100
    imprimir_matriz(matriz)
    
    # Variables para el máximo y mínimo con sus posiciones
    max_valor, min_valor = None, None
    pos_max, pos_min = (-1, -1), (-1, -1)
    
    # Buscar el máximo y el mínimo con sus posiciones
    for i in range(filas):
        for j in range(columnas):
            valor = matriz[i][j]
            if max_valor is None or valor > max_valor:
                max_valor = valor
                pos_max = (i, j)
            if min_valor is None or valor < min_valor:
                min_valor = valor
                pos_min = (i, j)
    
    print(f"\n💎 El número máximo es {max_valor}, en la posición [fila, columna]: {pos_max}")
    print(f"📉 El número mínimo es {min_valor}, en la posición [fila, columna]: {pos_min}")
    
    # Imprimir la columna donde se encuentra el máximo valor
    print(f"\n📊 Columna {pos_max[1]} (donde se encuentra el mayor valor):")
    for fila in matriz:
        print(fila[pos_max[1]])
    
    # Imprimir la fila donde se encuentra el máximo valor
    print(f"\n📋 Fila {pos_max[0]} (donde se encuentra el mayor valor):")
    print(matriz[pos_max[0]])
