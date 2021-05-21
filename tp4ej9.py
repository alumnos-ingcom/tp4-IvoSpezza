################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero_reintento

def es_primo(numero):
    
    numero = abs(numero)    # numeroP es solo para a la hora de comparar contador con numeroP no tener problema si el usuario ingreso un valor negativo
    contador = 2
    validador_primal = True     
    
    while validador_primal:
        
        numero_dividido = numero
        
        while numero_dividido > 0:
            
            numero_dividido -= contador
              
        if contador == numero:
            
            return(True)
        
        
        elif numero_dividido == 0:
            
            return(False)
        
        
        contador += 1
    
def prueba():
    
    es_primo(ingreso_entero_reintento("ingrese un numero entero, comprobaremos si es primo."))

if __name__ == "__main__":
    prueba()
    
    