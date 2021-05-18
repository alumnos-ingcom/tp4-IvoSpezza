################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def compara(numero, otro_numero):
    solo_numeros_enteros = True
    while solo_numeros_enteros:
        try:
            
            numero = int(input("ingrese valor 1: "))
            
            otro_numero = int(input("ingrese valor 2: "))
            
            solo_numeros_enteros = False
            
        except ValueError:
            
            print("solo valores enteros.")
            
    if numero > otro_numero:
        print("1")
    elif numero == otro_numero:
        print("0")
    else:
        print("-1")
            

def prueba():
    pass

if __name__ == "__main__":
    prueba()
    compara("", "")
    