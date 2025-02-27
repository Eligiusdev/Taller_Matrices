import random

# Método para llenar una matriz con números aleatorios
def llenar_matriz(filas, columnas, min_val=1, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(columnas)] for _ in range(filas)]

# Método para imprimir una matriz de forma legible
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{v:5}" for v in fila))

# Método para llenar una matriz con cadenas ingresadas por el usuario
def llenar_matriz_cadenas(filas, columnas):
    matriz = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            valor = input(f"Ingrese una cadena para la posición [{f},{c}]: ")
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Método para contar dígitos en cada posición de una matriz de cadenas
def contar_digitos_en_matriz(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    matriz_digitos = [[sum(char.isdigit() for char in str(matriz[f][c])) for c in range(columnas)] for f in range(filas)]
    return matriz_digitos

# Método para llenar una matriz con cadenas ingresadas por el usuario
def llenar_matriz_cadenas(filas, columnas):
    matriz = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            valor = input(f"Ingrese una cadena para la posición [{f},{c}]: ")
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Método para contar dígitos en cada posición de una matriz de cadenas
def contar_digitos_en_matriz(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    matriz_digitos = [[sum(char.isdigit() for char in str(matriz[f][c])) for c in range(columnas)] for f in range(filas)]
    return matriz_digitos
