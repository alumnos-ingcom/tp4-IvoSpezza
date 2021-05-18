################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def convertir_a_fahrrenheit(centigrados):
    validante = True
    
    while validante:
        try:
            centigrados = float(input("ingrese la t° ambiente en centigrados "))
            validante = False
        except ValueError:
            print(f"{centigrados} tiene que ser un numero, reintente")
    
    fahrenheit = (centigrados * 1.8) + 32
    
    print(f"{centigrados}° centigrados son {fahrenheit}° grados fahrenheit")
    
def convertir_a_centigrados(fahrenheit):
    validante = True
    
    while validante:
        try:
            fahrenheit = float(input("ingrese la t° ambiente en fahrenheit "))
            validante = False
        except ValueError:
            print(f"{fahrenheit} tiene que ser un numero, reintente")
    
    centigrados = (fahrenheit -32) / 1.8
    
    print(f"{fahrenheit}° grados fahrenheit son {centigrados}° centigrados ")
    
    
def prueba():
    pass

if __name__ == "__main__":
    prueba()
    convertir_a_fahrrenheit("")
    convertir_a_centigrados("")