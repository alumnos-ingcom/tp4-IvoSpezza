################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def ordenar_mayor_a_menor(uno, dos, tres):
    
    validador_de_n = True
    
    print("tupla de mayor a menor")
    
    while validador_de_n:
        try:
            uno = int(input("valor a "))
            dos = int(input("valor b "))
            tres = int(input("valor c "))
            validador_de_n= False
        except ValueError:
            print("tiene que ser un numero entero")
            
    lista =  [uno, dos , tres]
    
    lista.sort()
    lista.reverse()
    
    la_tupla = tuple(lista)
    
    return la_tupla
    
    
def ordenar_menor_a_mayor(uno, dos, tres):
    validador_de_n = True
    
    print("tupla de menor a mayor")
    
    while validador_de_n:
        try:
            uno = int(input("valor a "))
            dos = int(input("valor b "))
            tres = int(input("valor c "))
            validador_de_n= False
        except ValueError:
            print("tiene que ser un numero entero")
            
    lista =  [uno, dos , tres]
    
    lista.sort()
    
    la_tupla = tuple(lista)
    
    return la_tupla

    
def prueba():
    
    ordenar_mayor_a_menor("","","")
    
    ordenar_menor_a_mayor("","","")
    
if __name__ == "__main__":
    prueba()
    
    