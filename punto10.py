from Metodos import llenar_matriz_cadenas, imprimir_matriz, contar_digitos_en_matriz

def ejecutar_punto10():
    print("\n--- Ejercicio 10: Contar dígitos en una matriz de cadenas ---")
    
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    
    # Llenar la matriz con cadenas ingresadas por el usuario
    matriz_cadenas = llenar_matriz_cadenas(filas, columnas)
    
    print("\n📋 Matriz de Cadenas:")
    imprimir_matriz(matriz_cadenas)
    
    # Crear una segunda matriz con la cantidad de dígitos en cada posición
    matriz_digitos = contar_digitos_en_matriz(matriz_cadenas)
    
    print("\n🔢 Matriz con la cantidad de dígitos en cada posición:")
    imprimir_matriz(matriz_digitos)
