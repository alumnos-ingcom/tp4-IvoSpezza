################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def signo(numero):
    numerosiosi = True
    while numerosiosi:
        try:
            numero = int(input("Introduzca un valor negativo o positivo: "))
            numerosiosi = False
        except ValueError:
            print("valor no utilizable, reintente")
    if numero > 0:
        return("+")
    elif numero < 0:
        return("-")
    else:
        return(0)

def prueba():
    
    signo("")
    
if __name__ == "__main__":
    prueba()
    
    