################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero_reintento

def signo(numero):
    
    if numero > 0:
        return("+")
    elif numero < 0:
        return("-")
    else:
        return(0)

def prueba():
    
    numero = ingreso_entero_reintento("Introduzca un valor negativo o positivo: ")
    
    signo(numero)
    
    print(f" El numero '{numero}' es {signo(numero)}")
    
if __name__ == "__main__":
    prueba()
    
    