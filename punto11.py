from Metodos import llenar_matriz, imprimir_matriz

def ejecutar_punto11():
    print("\n--- Ejercicio 11: Análisis de calificaciones ---")
    
    estudiantes = int(input("Ingrese la cantidad de estudiantes (N): "))
    examenes = 5  # Siempre son 5 exámenes por estudiante
    
    # Llenar la matriz con calificaciones (entre 0 y 100)
    matriz_calificaciones = llenar_matriz(estudiantes, examenes, 0, 100)
    imprimir_matriz(matriz_calificaciones)
    
    # a. Calcular el promedio de cada estudiante
    promedios_estudiantes = [sum(fila) / examenes for fila in matriz_calificaciones]
    print(f"\n📊 Promedio de cada estudiante: {promedios_estudiantes}")
    
    # b. Estudiantes con la mejor calificación en la nota 3 (columna 2)
    nota3 = [fila[2] for fila in matriz_calificaciones]
    max_nota3 = max(nota3)
    estudiantes_mejor_nota3 = [i for i, nota in enumerate(nota3) if nota == max_nota3]
    print(f"\n🏆 Estudiantes con la mejor calificación en la nota 3: {estudiantes_mejor_nota3}")
    
    # c. Estudiantes con la mejor nota en el examen 1 (columna 0) y examen 5 (columna 4)
    nota1 = [fila[0] for fila in matriz_calificaciones]
    nota5 = [fila[4] for fila in matriz_calificaciones]
    
    max_nota1 = max(nota1)
    max_nota5 = max(nota5)
    
    mejores_nota1 = [i for i, nota in enumerate(nota1) if nota == max_nota1]
    mejores_nota5 = [i for i, nota in enumerate(nota5) if nota == max_nota5]
    
    print(f"\n✨ Estudiantes con la mejor nota en el examen 1: {mejores_nota1}")
    print(f"✨ Estudiantes con la mejor nota en el examen 5: {mejores_nota5}")
    
    # d. Determinar cuál de las notas tiene el promedio más alto entre todos los exámenes
    promedios_examenes = [sum(fila[i] for fila in matriz_calificaciones) / estudiantes for i in range(examenes)]
    mejor_examen = promedios_examenes.index(max(promedios_examenes))
    
    print(f"\n📈 Promedios de cada examen: {promedios_examenes}")
    print(f"📌 El examen con el promedio más alto es el examen {mejor_examen + 1}, con un promedio de {promedios_examenes[mejor_examen]:.2f}.")
