from validaciones import* 
import random


#1
def cargar_notas():

    matriz_notas = [[0] * 3 for _ in range(5)]  

    for participante in range(5): 
        print(f"Notas para el participante número {participante + 1}:")
        
        for jurado in range(3):  
            voto = input(f"Ingrese el voto del jurado número {jurado + 1} (1-100): ")
            voto = validar_voto(voto)  
            matriz_notas[participante][jurado] = voto
    
    return matriz_notas


#2
def mostrar_votos(matriz_notas):
    """Muestra los votos de cada participante.
    """
    print("\nResumen de Votos:")
    print(f"{'Participante':<15} {'Jurado 1':<10} {'Jurado 2':<10} {'Jurado 3':<10} {'Promedio':<10}")
    print("-" * 55)
    
    for i in range(len(matriz_notas)):  
        participante = i + 1
        notas = matriz_notas[i] 
        

        promedio = calcular_promedio(notas)


        print(f"{participante:<15} {notas[0]:<10} {notas[1]:<10} {notas[2]:<10} {promedio:<10.2f}")


def calcular_promedio(notas): 
    """Calcula el promedio de los votos de un solo participante (jurado 1, 2 y 3).
    """
    total_notas = 0
    for i in range(len(notas)):  
        total_notas += notas[i]
    promedio = total_notas / len(notas)  
    return promedio


#3
def ordenar_por_promedio(matriz_notas, orden):
    """
    Ordena la matriz de notas de los participantes por su promedio de notas, puede ser ascendente o descendente.
    """

    promedios = []

    for i in range(len(matriz_notas)):
        promedio = calcular_promedio(matriz_notas[i])
        promedios.append((i, promedio)) 


    for i in range(len(promedios)):
        for j in range(i + 1, len(promedios)):
            if (orden == 'asc' and promedios[i][1] > promedios[j][1]) or (orden == 'desc' and promedios[i][1] < promedios[j][1]):
                promedios[i], promedios[j] = promedios[j], promedios[i]

    matriz_notas_ordenadas = [matriz_notas[i[0]] for i in promedios]

    return matriz_notas_ordenadas


#4
def calcular_tres_peores(matriz_notas):
    """
    Calcula los tres peores participantes basados en su promedio de notas.
    Devuelve una lista de los tres peores participantes y sus notas.
    """
    participantes_con_notas = [(i + 1, matriz_notas[i]) for i in range(len(matriz_notas))]
    

    for i in range(len(participantes_con_notas)):
        for j in range(len(participantes_con_notas) - 1):
            promedio_j = calcular_promedio(participantes_con_notas[j][1])
            promedio_j1 = calcular_promedio(participantes_con_notas[j + 1][1])
            
            if promedio_j > promedio_j1:
                participantes_con_notas[j], participantes_con_notas[j + 1] = participantes_con_notas[j + 1], participantes_con_notas[j]
    

    return participantes_con_notas[:3]


def mostrar_tres_peores(matriz_notas):
    """
    Muestra los 3 peores participantes basados en su promedio de notas.
    """
    tres_peores = calcular_tres_peores(matriz_notas)
    print("\nLos 3 peores participantes:")
    print(f"{'Participante':<15} {'Jurado 1':<10} {'Jurado 2':<10} {'Jurado 3':<10} {'Promedio':<10}")
    print("-" * 55)
    
    for participante, notas in tres_peores:
        promedio = calcular_promedio(notas)

        print(f"{participante:<15} {notas[0]:<10} {notas[1]:<10} {notas[2]:<10} {promedio:<10.2f}")

#5
def mostrar_mayores_promedios(matriz_notas):
    """
    Muestra los participantes que tienen un promedio superior al promedio total de todos.
    """
    promedio_total = calcular_mayor_promedio(matriz_notas)
    
    print(f"\nPromedio total de todos los participantes: {promedio_total:.2f}")
    print("\nParticipantes con promedio superior al promedio total:")
    print(f"{'Participante':<15} {'Jurado 1':<10} {'Jurado 2':<10} {'Jurado 3':<10} {'Promedio':<10}")
    print("-" * 55)
    
  
    for i in range(len(matriz_notas)):
        participante = i + 1
        notas = matriz_notas[i]
        

        promedio = calcular_promedio(notas)
        

        if promedio > promedio_total:
            print(f"{participante:<15} {notas[0]:<10} {notas[1]:<10} {notas[2]:<10} {promedio:<10.2f}")


def calcular_mayor_promedio(matriz_notas): 
    """
    Calcula el promedio de todos los participantes y muestra aquellos con un promedio superior al promedio total.
    """

    total_participantes = len(matriz_notas)
    acumulador_total_notas = 0

    for notas in matriz_notas:
        acumulador_total_notas += calcular_promedio(notas)  

    promedio_total = acumulador_total_notas / total_participantes  
    return promedio_total

#6
def mostrar_jurado_malo(matriz_notas):
    """
    Muestra el jurado o los jurados que pusieron en promedio las peores notas.
    """
 
    promedios_jurados = [0] * 3
    

    for i in range(len(matriz_notas)): 
        for j in range(3):  
            promedios_jurados[j] += matriz_notas[i][j]
    

    for j in range(3):
        promedios_jurados[j] /= len(matriz_notas) 
    

    peor_promedio = min(promedios_jurados)
    

    print("\nJurado(s) con el peor promedio de notas:")
    for jurado in range(3):
        if promedios_jurados[jurado] == peor_promedio:
            promedio = int(promedios_jurados[jurado] * 100) / 100.0
            print(f"Jurado {jurado + 1} con un promedio de {promedio}")


def calcular_promedio_jurado(matriz_notas, jurado):
    """
    Calcula el promedio de las notas dadas por un jurado específico.
    """
    total_notas = 0
    num_participantes = len(matriz_notas)
    

    for i in range(num_participantes):
        total_notas += matriz_notas[i][jurado] 
    

    promedio_jurado = total_notas / num_participantes
    return promedio_jurado

#
def mostrar_por_sumatoria(matriz_notas):
    """
    Muestra los participantes cuya suma de notas sea igual al número dado por el usuario.
    """

    suma_buscada = 0
    while not validar_numero_sumatoria(suma_buscada):  
        suma_buscada = int(input("Ingrese un número entre 3 y 300: "))
        if not validar_numero_sumatoria(suma_buscada):  
            print("Reingrese un número dentro del rango solicitado (3 a 300).")


    encontrado = False


    for i in range(len(matriz_notas)):
        suma_notas = 0
        for nota in matriz_notas[i]:
            suma_notas += nota


        if suma_notas == suma_buscada:
            participante = i + 1 
            notas = matriz_notas[i]
            print(f"El participante número {participante}: obtuvo {suma_notas} de nota.") 
            encontrado = True
    

    if not encontrado:
        print("Ningun participante obtuvo esa nota.")


def calcular_promedio_participante(notas):
    """
    Calcula el promedio de un participante basado en sus notas.
    """
    total_notas = 0
    for nota in notas:
        total_notas += nota
    return total_notas / len(notas)

#8
def inicializar_votos(ganadores_iniciales):
    """
    Inicializa un contador de votos para cada participante,
    asignando un voto de inicio de 0 a cada uno de los ganadores.
    """
    votos = [0] * len(ganadores_iniciales)
    return votos


def definir_ganador_inicial(matriz_notas):
    """
    Determina el ganador inicial basado en el promedio de las notas.
    Si hay empate, devuelve una lista con los participantes empatados.
    """
    promedio_mayor = -1  
    ganadores_iniciales = [] 


    for i in range(len(matriz_notas)):
        promedio = calcular_promedio_participante(matriz_notas[i]) 
        if promedio > promedio_mayor:
            promedio_mayor = promedio  
            ganadores_iniciales = [i + 1]  
        elif promedio == promedio_mayor:
            ganadores_iniciales.append(i + 1)  

    return ganadores_iniciales, promedio_mayor  


def desempate(ganadores_iniciales, matriz_notas):
    """
    Realiza el desempate entre los ganadores iniciales, basándose en la elección de los jurados.
    Si hay un empate, el ganador se elige de manera aleatoria.
    """

    votos = inicializar_votos(ganadores_iniciales)


    for jurado in range(3):  
        while True:
            print(f"\nJurado {jurado + 1}, elija a uno de los siguientes ganadores: {ganadores_iniciales}")
            eleccion = input("Ingrese el número del participante elegido: ").strip()


            if eleccion.isdigit() and int(eleccion) in ganadores_iniciales:

                for i in range(len(ganadores_iniciales)):
                    if ganadores_iniciales[i] == int(eleccion):
                        votos[i] += 1
                        break
                break
            else:
                print("Opción no válida. Elija un número válido de los ganadores.")


    mas_votos = -1
    ganadores_finales = []
    for i in range(len(votos)):
        if votos[i] > mas_votos:
            mas_votos = votos[i]
            ganadores_finales = [ganadores_iniciales[i]]  
        elif votos[i] == mas_votos:
            ganadores_finales.append(ganadores_iniciales[i])  


    if len(ganadores_finales) == 1:
        return ganadores_finales[0]
    else:
        print("\nDebido a que hubo un empate el ganador se elegirá de manera aleatoria.")
        return random.choice(ganadores_finales)


def mostrar_ganador_final(matriz_notas):
    """
    Determina el ganador final de la competencia, incluyendo el desempate si es necesario.
    """

    ganadores_iniciales, promedio_mayor = definir_ganador_inicial(matriz_notas)
    

    if len(ganadores_iniciales) == 1:
        ganador_final = ganadores_iniciales[0]
    else:

        ganador_final = desempate(ganadores_iniciales, matriz_notas)
    

    print(f"El ganador final es el participante número {ganador_final} con un promedio de {promedio_mayor:.2f} puntos.")
    
    return ganador_final, promedio_mayor






