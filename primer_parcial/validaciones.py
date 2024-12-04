def validar_voto(voto):
    """
    Valida que el voto ingresado esté entre 1 y 100.
    Si es inválido, solicita nuevamente el voto.
    """
    while True:
        if voto.isdigit() and 1 <= int(voto) <= 100:
            return int(voto)
        else:
            print("Error. El voto debe ser un número entre 1 y 100.")
            voto = input("Reingrese el voto: ")


def validar_orden():
    """ Valida si la opción ingresada es 'asc' o 'desc'.
    Si no es válida, solicita que se ingrese una opción válida.
    """
    orden = input("¿Desea ordenar los resultados de manera ascendente o descendente? (asc/desc): ").strip().lower()
    
    while orden not in ['asc', 'desc']:
        print("Opción inválida.")
        orden = input("¿Desea ordenar los resultados de manera ascendente o descendente? (asc/desc): ").strip().lower()
    
    return orden



def validar_numero_sumatoria(numero):
    """
    Valida que el número esté en el rango entre 3 y 300.
    """

    if numero < 3 or numero > 300:
        return False
    return True


