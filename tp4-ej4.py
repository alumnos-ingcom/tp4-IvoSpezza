################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero_reintento

def compara(numero, otro_numero):
            
    if numero > otro_numero:
        return(1)
    elif numero == otro_numero:
        return(0)
    else:
        return(-1)
            

def prueba():
      
    numero = compara(ingreso_entero_reintento("ingrese un numero entero,"), ingreso_entero_reintento("ingrese otro numero entero,"))
    
    print(numero)
    
if __name__ == "__main__":
     prueba()
    