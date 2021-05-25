################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio



def creador_de_listas():

    lista = []
    error = ("el valor ingresado debia ser un numero entero!")
    validante_de_enteros = True
    
    while validante_de_enteros:
        try:
            cantidad = int(input("¿Cuantos valores quiere en su lista? "))
            if cantidad < 0:
                cantidad = cantidad * -1
                print(f"no se aceptan numero negativos, el valor {cantidad*-1} ahora es {cantidad}")
            elif cantidad == 0:
                cantidad += 1
                print("0 no es aceptado, tu lista tendra 1 solo valor")
            validante_de_enteros = False
        except ValueError:
            print(error)
    
    variable_para_el_mensaje = cantidad
    
    validante_de_enteros = True
    
    while validante_de_enteros:
        try:
            while cantidad > 0:
                lista.append(int(input(f"ingrese el valor entero n°{variable_para_el_mensaje - cantidad +1 } : ")))
                cantidad -= 1
            validante_de_enteros = False
            return lista
        except ValueError:
            print(error)

def minimo(lista):
    
    print(f"esta es tu lista: {lista}")
    numero_menor = lista[0]
   
    for i in lista:
        if numero_menor > i:
            numero_menor = i
                
            
            
        
    print(f"el menor numero en la lista indicada es: {numero_menor}")
    
    
    return(numero_menor)
    
    
    
    
    
def maximo(lista):
    
    print(f"esta es tu lista: {lista}")
    
    
    numero_mayor = lista[0]
   
    for i in lista:
        if numero_mayor < i:
            numero_mayor = i
            
    print(f"el mayor numero en la lista indicada es: {numero_mayor}")
    
    
    return(numero_mayor)




def prueba():
    
    lista_creada = creador_de_listas()
    
    minimo(lista_creada)
    maximo(lista_creada)
    
if __name__ == "__main__":
    prueba()
    
    