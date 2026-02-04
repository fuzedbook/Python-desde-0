#creando funcion que suma numeros
def sumar():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2:")
        #intentando convertirlos a enteros y sumarlos
        try:
         resultado = int(a) + int(b)
        #Si lanzo una excepcion , pedirle que reingrese los datos   
        except Exception as e :
            print("Te pedi un numero")
            print(f" Error : {type(e)}")
            #si todo salio bien terminamos el bucle
        else:
            break
        #Mostrando el resultado
    return resultado
print(sumar())

#Lanzando mi propia excepcion
class MiExcepcion(Exception):
    def __innit__(self,err):
        print(f"El error es {err}")
    
#Manejando mi excepcion    
try:
    raise MiExcepcion("Te equivocaste")
except:
    print("Como te equivocas en eso")