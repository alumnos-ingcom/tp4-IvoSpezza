################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def suma_lenta(numero, otro_numero):
    
    validador_de_n = True
    
    while validador_de_n:
        try:
            numero = int(input("valor a "))
            otro_numero = int(input("valor b "))
            validador_de_n= False
        except ValueError:
            print("tiene que ser un numero entero")
    print(f"Procesando {numero} + {otro_numero} ...")
    
    resultado = numero + otro_numero
    suma_lenta = 0
    
    if numero < otro_numero:
        suma_lenta = numero
    else:
        suma_lenta = otro_numero
    
    while suma_lenta < resultado:
        print(f"{suma_lenta}")
        suma_lenta += 1
    print(f"{suma_lenta}")
    print("proceso terminado.")
def prueba():
    pass

if __name__ == "__main__":
    prueba()
    suma_lenta("", "")
    