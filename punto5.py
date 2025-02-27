from Metodos import llenar_matriz, imprimir_matriz

def ejecutar_punto5():
    print("\n--- Ejercicio 5: Almacenar la matriz en un vector ---")
    
    filas, columnas = 5, 5
    matriz = llenar_matriz(filas, columnas, 1, 100)  # Números aleatorios entre 1 y 100
    imprimir_matriz(matriz)
    
    # Convertir la matriz en un vector lineal
    vector_resultante = [elemento for fila in matriz for elemento in fila]
    
    print(f"\n📦 Vector resultante: {vector_resultante}")
