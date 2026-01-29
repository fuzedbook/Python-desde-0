contador = 0

#mientras que la condicion se cumpla, el bucle va a seguir ejecutando,
#Vuelta tras vuelta se verifica la condicion
while contador < 10:
    contador += 1
    print(contador)
    
    
    
#Funciones

numeros = [3, 5, 6, 7, 94, 65]

#Encontrando el numero mas alto
numero_mas_alto = max(numeros)

#Encontrando el numero mas pequeño
numero_mas_chico = min(numeros)

#Redondeando a 6 decimales
numero = round(13.45678, 4)

#muestra false cuando es 0, None, lista vacia o false, pero muestra true cuando es un numero diferente a 0, true, una lista con algo o valores no vacios
resultado = bool(None)

#regresta true, si todos los valores, son verdaderos, va item por item de la lista revisando , si alguno es falso, regresa false
resultado_all = all([ True, 1, "true", [5, 7]])

#suma todos los valores de un iterable
suma = sum(numeros)


#Creando una funcion simple
def saludar():
    print("Hola que tal")
#saludar()

#crear una funcion que tenga parametros
def saludo(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "rey"
    else:
        adjetivo = "algo"
    print(f"Hola {nombre}, mi {sexo} como estas?")

#saludo("oscar","hombre")

#crear una funcion que retorne valores
#num = input()
#def calculo(num):
 #   listado = "abcdefghij"
 #   entero =str(num)
 #   num = int(entero[0])
 #   c1 = num - 2
 #   c2 = num
 #   c3 = num - 5
 #  contraseña = f"{listado[c1]}{listado[c2]}{listado[c3]}{num*2}"
 # return contraseña
#password = calculo(num)
#frase = f"Tu contraseña neuva es {password}"
#print (frase)

#Forma no optima de sumar valores
def summa(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
resultadoo = summa([1,2,3,4,5,6])
print(resultadoo)

#forma optima de sumar valores
def suma_total(numeross):
    return sum([*numeross])
resultado_2 = suma_total([3,4,5,6,7])
print(resultado_2)


#lo mismo que arriba pero utilizando el operador * como parametro (args)

def suma(nombre, *numb):
    return f"{nombre}, la suma de tus numeros es : {sum(numb)}"

resultado_3 = suma("oscar", 1,2,3,4,5,6,7)
print(resultado_3)

#Creando una funcion de 3 parametros

def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido}, eres muy {adjetivo}'
frasse = frase("Oscar","fierros","inteligente")
print(frasse)

#utilizando keyword arguments
#frasse = frase(adjetivo="inteligente",nombre="Oscar",apellido="Fierros")

#Creando la misma funcion con un parametro opcional y un valor por defecto
def fraase(nombre, apellido, adjetivo="inteligente"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"
frase_resultado = fraase("Oscar", "Fierros", "tonto")
print(frase_resultado)