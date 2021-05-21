################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero_reintento

from tp4ej9 import es_primo

def factores_primos(numero):
    
    lista = []
    contador = 2
    validador_factores_primos = True
    
    while validador_factores_primos:
        numero_en_prueva = abs(numero)
    
        if contador == numero_en_prueva:
            
            validador_factores_primos = False
    
    
        while numero_en_prueva > 0:
            numero_en_prueva -= contador
        
        
        
        if numero_en_prueva == 0:
            
            factor_primo = es_primo(contador)    
            
            if factor_primo:
            
                lista.append(contador)
              
        contador += 1
        
    factores_primos = tuple(lista)
    
    return factores_primos

def prueba():
    
    entero = ingreso_entero_reintento("ingrese un numero entero,")
    
    tupla_de_factores = factores_primos(entero)
    
    print(f"los factores primos de '{entero}' son {tupla_de_factores}")

if __name__ == "__main__":
    prueba()
    
    