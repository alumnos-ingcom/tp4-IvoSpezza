################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero_reintento



def ordenar_mayor_a_menor(uno, dos, tres):
            
    lista = [uno, dos , tres]
    lista.sort()
    lista.reverse()
    la_tupla = tuple(lista) 
    return la_tupla    
    
def ordenar_menor_a_mayor(uno, dos, tres):
            
    lista =  [uno, dos , tres]
    lista.sort() 
    la_tupla = tuple(lista)   
    return la_tupla

def prueba():
    
    valorA = ingreso_entero_reintento("ingrese valor A,")
    valorB = ingreso_entero_reintento("ingrese valor B,")
    valorC = ingreso_entero_reintento("ingrese valor C,")   
    ordenadoMm = ordenar_mayor_a_menor(valorA, valorB, valorC)
    ordenadomM = ordenar_menor_a_mayor(valorA, valorB, valorC)
    print(f"la tuple: '{valorA}, {valorB}, {valorC}' ordenada de mayor a menor = {ordenadoMm} , de menor a mayor = {ordenadomM}")
    
if __name__ == "__main__":
    prueba()
    
    