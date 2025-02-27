from Metodos import llenar_matriz, imprimir_matriz
import random

def ejecutar_punto7():
    print("\n--- Ejercicio 7: Contar ceros, positivos y negativos en una matriz 5x6 ---")
    
    filas, columnas = 5, 6
    # Se genera una matriz con números aleatorios entre -50 y 50 (incluyendo negativos, ceros y positivos)
    matriz = [[random.randint(-50, 50) for _ in range(columnas)] for _ in range(filas)]
    imprimir_matriz(matriz)
    
    # Contadores
    ceros = positivos = negativos = 0
    
    # Recorrer la matriz y contar los tipos de números
    for fila in matriz:
        for numero in fila:
            if numero == 0:
                ceros += 1
            elif numero > 0:
                positivos += 1
            else:
                negativos += 1
    
    print(f"\n🔢 Cantidad de ceros: {ceros}")
    print(f"📈 Cantidad de positivos: {positivos}")
    print(f"📉 Cantidad de negativos: {negativos}")
