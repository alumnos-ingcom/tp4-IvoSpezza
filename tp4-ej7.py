################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero_reintento

def division_lenta(dividendo, divisor):
    
    cociente = 0
    if dividendo > 0 and divisor < 0 or dividendo < 0 and divisor > 0:
        
        resto = abs(dividendo)
        divisor = abs(divisor)
        
        while resto > 0:
            
            resto -= divisor
            cociente += 1
             
        cociente = -1 * cociente
        resto= -1 * resto
        lista = [cociente, resto]
        return lista
    elif divisor == 0 or dividendo == 0:
        
        raise error_de_division("error al dividir por 0")
        
    else:
        
        resto = abs(dividendo)
        divisor = abs(divisor)
        while resto > 0:
            
            resto -= divisor
            cociente += 1
        
        lista = [cociente, resto]
        return lista

class error_de_division(Exception):
    pass

def prueba():
    
    cociente_resto = division_lenta\
                     (ingreso_entero_reintento("ingrese valor a dividir"), \
                      ingreso_entero_reintento("ingrese divisor")) 

    print(f"el cociente y el resto son {cociente_resto}")

if __name__ == "__main__":
    prueba()   