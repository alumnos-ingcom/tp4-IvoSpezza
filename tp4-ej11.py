################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
def es_palindromo(texto):

    palindro = list(texto)

    palindro_reverse = palindro.reverse()
    
    if palindro == palindro_reverse:
        
        return True
    
    elif palindro != palindro_reverse:
        
        return False
    
def prueba():
    
    palabra = input("ingrese una palabra ")
    
    if es_palindromo(palabra):
    
        print(f"la palabra {palabra} es palindroma")
    
    else:
        
        print(f"la palabra {palabra} NO es palindroma")
        
        
if __name__ == "__main__":
    prueba()
    
    