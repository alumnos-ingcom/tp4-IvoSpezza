################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from tp4ej1 import ingreso_entero_reintento


def suma_lenta(numero, otro_numero):
    
    resultado = numero + otro_numero
    suma_lenta = 0
    
    if numero < otro_numero:
        suma_lenta = numero
    else:
        suma_lenta = otro_numero
    
    while suma_lenta < resultado:
        
        print(f"{suma_lenta}")
        suma_lenta += 1
    print(f"{suma_lenta}")
    
def prueba():
    
    suma_lenta(ingreso_entero_reintento("ingrese valor a, "), ingreso_entero_reintento("ingrese valor b, ")) 
    
if __name__ == "__main__":
    prueba()
    
    