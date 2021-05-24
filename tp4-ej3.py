################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio



def numerofloat(mensaje):

    validante = True
    while validante:
            
        numerof = input(mensaje)
        try:
                
            numerof = float(numerof)
            validante = False
            
            return numerof
        
        except ValueError:
            print(f"{numerofloat} tiene que ser un numero, reintente")
            
            
def convertir_a_fahrenheit(centigrados):
     
    
    fahrenheit = (centigrados * 1.8) + 32
    
    
    
    return fahrenheit

def convertir_a_centigrados(fahrenheit):
    
    centigrados = (fahrenheit -32) / 1.8
    
    print(f"{fahrenheit}° grados fahrenheit son {centigrados}° centigrados ")
    return centigrados
    
def prueba():
    
    faherein = convertir_a_fahrenheit(numerofloat("ingrese un valor en centigrados, se trasformara en fahrenheit "))
    
    centigradin = convertir_a_centigrados(numerofloat("ingrese un valor en fahrenheit, se transformara en centigrados "))
    
    print(f"los centigrados ingreados equivalen a {faherein}° grados fahrenheit")
    
    print(f"los fahrenheit ingreados equivalen a {centigradin}° grados centigrados")
               
if __name__ == "__main__":
    prueba()
    