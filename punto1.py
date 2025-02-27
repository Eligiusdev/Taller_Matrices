from Metodos import llenar_matriz, imprimir_matriz

def ejecutar_punto1():
    print("\n--- Ejercicio 1: Suma de números en una matriz 6x6 ---")
    
    filas, columnas = 6, 6
    matriz = llenar_matriz(filas, columnas)
    imprimir_matriz(matriz)
    
    suma = sum(sum(fila) for fila in matriz)
    print(f"\n✅ La suma de todos los números en la matriz es: {suma}")
