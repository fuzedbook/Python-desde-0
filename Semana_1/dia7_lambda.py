numeros = [1,2,3,4,5,6,7,8,9]

#Creando funcion lambda para multiplicar por dos
multiplicar_dos = lambda x : x*2

#Creando funcion comun que diga si es par o no
def es_par(num):
    if (num%2==0):
        return True

#Usando filter con una funcion comun
numeros_pares = filter(es_par, numeros)

#Creando lo mismo pero con lambda
numeross_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeross_pares))

#funcion para obtener al asistente y al profesor segun la edad
def obtener_compañeros(cantidad):
    #Creando la lista con los compañeros
    compañeros = []

    #Ejecutando un for para pedir informacion de cada compañero
    for i in range(7):
        nombre = input("ingrese el nombre del compañero")
        edad = int(input("Ingrese la edad del compañero"))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista con .append
        compañeros.append(compañero)
    #ordenandolos de menor a mayor segun la edad
    compañeros.sort(key=lambda x : x[1])
    
    #Compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor    
    asistente = compañeros[0][0]#Ya ordenados elejimos al primero, el mas chico
    profesor = compañeros[-1][0]#elejimos al ultimo, el mas grande
    #retornamos una tupla
    return asistente,profesor
#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)
#mostrando el resultado
print(f"El asistente es : {asistente} y el profesor es : {profesor}")