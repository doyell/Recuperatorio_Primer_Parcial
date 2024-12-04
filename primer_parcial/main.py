from funciones import*
from validaciones import*



def main():
    matriz_notas = []  

    while True:  
        print("\nIngrese una opción:\n1. Cargar notas\n2. Mostrar votos\n3. Ordenar votos (ascendente o descendente)\n4. Mostrar los peores 3\n5. Mostrar los mayores promedios\n6. Mostrar jurado malo\n7. Mostrar por sumatoria (entre 3 y 300)\n8. Definir el ganador\n9. Salir")
        
        opcion = input("Seleccione una opción del 1 al 9: ").strip()

        match opcion:
            case "1":
                matriz_notas = cargar_notas()  
            case "2":
                if not matriz_notas:
                    print("Primero debe cargar las notas")
                else:
                    mostrar_votos(matriz_notas)
            case "3":
                if not matriz_notas:
                    print("Primero debe cargar las notas.")
                else:
                    orden = validar_orden()
                    matriz_notas_ordenadas = ordenar_por_promedio(matriz_notas, orden)
                    mostrar_votos(matriz_notas_ordenadas)
            case "4":
                if not matriz_notas:
                    print("Primero debe cargar las notas.")
                else:
                    mostrar_tres_peores(matriz_notas) 
            case "5":
                if not matriz_notas:
                    print("Primero debe cargar las notas.")
                else:
                    mostrar_mayores_promedios(matriz_notas) 
            case "6":
                if not matriz_notas:
                    print("Primero debe cargar las notas.")
                else:
                    mostrar_jurado_malo(matriz_notas) 
            case "7":
                if not matriz_notas:
                    print("Primero debe cargar las notas.")
                else:
                    mostrar_por_sumatoria(matriz_notas) 
            case "8":
                if not matriz_notas:
                    print("Primero debe cargar las notas.")
                else:
                    ganador_final, promedio_mayor = mostrar_ganador_final(matriz_notas)
            case "9":    
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Ingrese un número entre 1 y 9.")  

main()

