################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def division_lenta(dividendo, divisor):
    validante = True
    while validante:
        try:
            dividendo = int(input("ingrese valor a dividir "))
            divisor = int(input("ingrese divisor "))
            validante = False
        except ValueError:
            print("el valor ingresado debe ser un numero")
    
    cociente = 0
    if dividendo > 0 and divisor < 0 or dividendo < 0 and divisor > 0:
        
        resto = abs(dividendo)
        divisor = abs(divisor)
        
        while resto > 0:
            resto -= divisor
            cociente += 1
            
        cociente = -1 * cociente
        print(f"al dividir '{dividendo}' por '{divisor}', obtenemos como cociente '{cociente}' y como resto '{resto}'")
        
    elif divisor == 0 or dividendo == 0:
        
        print("ERROR FATAL, error al dividir por 0")
        
    elif dividendo > 0 and divisor > 0:
        
        resto = dividendo
        while resto > 0:
            resto -= divisor
            cociente += 1
        print(f"al dividir '{dividendo}' por '{divisor}', obtenemos como cociente '{cociente}' y como resto '{resto}'")


def prueba():
    
    division_lenta("","")   

if __name__ == "__main__":
    prueba()
    
    