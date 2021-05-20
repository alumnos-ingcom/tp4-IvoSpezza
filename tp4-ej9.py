################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def es_primo(numero):
    validante = True
    while validante:
        try:
            
            numero = int(input("Ingrese un numero entero "))
            validante = False
        except ValueError:
            print("error, intente otra vez")
    
    numeroP = abs(numero)    # numeroP es solo para a la hora de comparar contador con numeroP no tener problema si el usuario ingreso un valor negativo
    contador = 2
    validador_primal = True     
    
    while validador_primal:
        
        numero_dividido = numeroP
        
        while numero_dividido > 0:
            
            numero_dividido -= contador
        
        contador += 1
            
        
        if numero_dividido == 0:
            
            return(False)
            
            validador_primal = False
    
        elif contador == numeroP:
            
            return(True)
            
            validador_primal = False
    
    
    
def prueba():
    
    es_primo("")

if __name__ == "__main__":
    prueba()
    
    