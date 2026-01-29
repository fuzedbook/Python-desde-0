#Se cuenta del 0 al 9


#Creando una lista la cual si se puede modificar
lista = ["Oscar", "Fierros", True, 1.80]
#Esto es una tupla, tipo de lista solo que no se puede modificar
tuple = ("Oscar", "Fierros", True, 1.80)

#Valido :
#lista[5] = equis
#print(lista[5])

#No valido:
#tuple[3] = "hola"

#Nuevo conjunto (Set) esta en desorden, es como una lista pero no puedes repetir datos y te los da random

conjuntoset = {"Oscar", "Fierros", True, 1.80} #Recordar que te da los datos aleatorios y no puedes cambiar los datos mas adelante

#print(conjunto[0]) No funciona por que tu no puedes acceder a su indice

#Diccionario
#La estructura es clave : valor
#Siempre separados por comas
diccionario = {
    'nombre' : "Oscar",
    'canal' : 'No tengo',
    'Edad' : 17,
    'Emocionado' : True
    
}
#print(diccionario["Emocionado"])

#Operadores aritmeticos = Matematicas

#Suma y resta
suma = 12 + 5
resta = 12 - 5

#Multiplicacion y division
multi = 12 * 5
div = 12 / 5

#Exponentes
exponente = 12**5

#Division baja (//) Devuelve entero redondeado hacia abajo
divBaja= 12//5

#Resto o modulo - Nos muestra lo que sobra de las divisiones
resto = 12%5

#type(dato) nos muestra que tipo de dato es  ex, type(exponente), type(div)

#print(type(div))

#Operadores de comparacion

#Solo devuelven true o false

igualQue = 5 == 6

distintoQue = 5 != 6

menorQue = 5<6

mayorQue = 5>6

menorIgual = 5<=6

mayorIgual = 5>= 6

#Calculos combinados 

a = 5
b = 10
c = 20

comparacion = a + b > c

#Comparar usuarios
contraseña_guardada = "1435"
contraseña_escrita = "1435"

#print(contraseña_escrita == contraseña_guardada)

#Condicionales
edad = 17

#if condicion :
    #valor

if edad >= 18 :
    print("puedes pasar")
else :
    print("No puedes pasar")


if contraseña_guardada == contraseña_escrita :
    print("iniciando sesion...")
else :
    print("Incorrecto vuelva a intentar")
    
    
#if anidados y else if (elif)
ingreso = 50000
gasto = 48000

if ingreso > 10000 :
    if ingreso - gasto < 0:
        print("Estas al borde")
    elif ingreso - gasto > 3000:
        print("Estas bien")
    else :
        print("Estas gastando mucho")
elif ingreso >1000:
    print("Cuida tu dinero")
else :
    print("Te quedaste sin dinero")
    

#Miniproyecto final
listaa = ["Oscar", "Diego", "Johan"]
dicci = {
    "nombre" : listaa[0],
    "edad" : 18
}

if dicci["nombre"] == lista[0] :
    if dicci["edad"] >= 18 :
        print("Acceso permitido")
    else :
        print("Acceso denegado, menor de edad")
else :
    if dicci["edad"] < 18 :
        print("Nombre o edad no permitida")
    else :
        print("Edad permitida nombre incorrecto")

