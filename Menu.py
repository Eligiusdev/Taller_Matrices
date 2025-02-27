from punto1 import ejecutar_punto1
from punto2 import ejecutar_punto2
from punto3 import ejecutar_punto3
from punto4 import ejecutar_punto4
from punto5 import ejecutar_punto5
from punto6 import ejecutar_punto6
from punto7 import ejecutar_punto7
from punto8 import ejecutar_punto8
from punto9 import ejecutar_punto9
from punto10 import ejecutar_punto10
from punto11 import ejecutar_punto11

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    for i in range(1, 12):
        print(f"{i}. Ejecutar Punto {i}")
    print("0. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            ejecutar_punto1()
        elif opcion == "2":
            ejecutar_punto2()
        elif opcion == "3":
            ejecutar_punto3()
        elif opcion == "4":
            ejecutar_punto4()
        elif opcion == "5":
            ejecutar_punto5()
        elif opcion == "6":
            ejecutar_punto6()
        elif opcion == "7":
            ejecutar_punto7()
        elif opcion == "8":
            ejecutar_punto8()
        elif opcion == "9":
            ejecutar_punto9()
        elif opcion == "10":
            ejecutar_punto10()
        elif opcion == "11":
            ejecutar_punto11()
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Por favor, elija una opción del 0 al 11.")

if __name__ == "__main__":
    ejecutar_menu()
