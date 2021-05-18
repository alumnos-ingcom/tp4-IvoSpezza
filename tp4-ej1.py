################
# Ivo Spezzacatena - @IvoSpezza
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio



def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
   
    while cantidad_reintentos != 0:
        
        numero = input(f"{mensaje} tienes {cantidad_reintentos} intentos ")
        
        try:
            numero_entero = int(numero)
            print(f"{numero}, Buen numero Geniall!!!!!!!")
            break
        
        except ValueError as err:
            
            cantidad_reintentos -= 1
            
            if cantidad_reintentos > 0:
                
                print(f"te queda {cantidad_reintentos} intentos, no falles!!!")
                
            else:
                
                raise IngresoIncorrecto("fallaste 5 veces seguidas... increible") from err




def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    ciclo = True
    while ciclo:
        numero = input(mensaje)
        try:
            valor = int(numero)
            if valor > valor_minimo and valor < valor_maximo:
                print(f"0 < {valor} < 10")
                ciclo = False
            elif valor < valor_minimo:
                print(f"el numero tiene que ser mayor a {valor_minimo}")
            elif valor > valor_maximo:
                print(f"el numero tiene que ser menor a {valor_maximo}")
        except ValueError as err:
            raise IngresoIncorrecto("no ingresaste un numero... intenta otra vez") from err
      
            

class IngresoIncorrecto(Exception):
    pass

def prueba():
    pass

if __name__ == "__main__":
    prueba()
    ingreso_entero_reintento("ingrese numero entero,", )
    ingreso_entero_restringido("ingrese un valor entero entre 0 y 10")