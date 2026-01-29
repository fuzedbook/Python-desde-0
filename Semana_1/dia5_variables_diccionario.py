#creando tuplas con tuple()
tupla = tuple(["dato1", "dato2"])

#creando una tupla sin parentesis con varios datos
tupla = "dato1", "dato2"

#creando una tupla sin parentesis de un solo dato
tupla = "dato",

#print(type(tupla))

#Creando un conjunto con set()
conjunto = set(["Dato 1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato 2"])
conjunto2 = {conjunto1,"dato3"}

#print(conjunto2)


#Teoria de conjuntos
conjunto11 = {1,3,5,7}
conjunto22 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto22.issubset(conjunto11)

#verificando si es un superconjunto
resultado = conjunto22.issuperset(conjunto11)

#verificar si hay un numero en comun
resultado = conjunto22.isdisjoint(conjunto11)

#print(resultado)


#creando diccionarios con dict()
diccionario = dict(nombre="Oscar", edad= "17")

#las listas no pueden ser keys y usamos frozenset para meter conjuntos
diccionario = {frozenset(["oscar","algo"]):"algos"}

#Creando diccionarios con fromkeys() valor por defecto : none
diccionario = dict.fromkeys(["nombre", "edad"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "edad"], "nose")

#print(diccionario)



materias = {
    "matematicas": 80,
    "ingles": 74,
    "programacion": 100
}

suma = 0
contador = 0
for valor in materias.values():
    suma+=valor
    contador+=1
promedio = (suma/contador)



if promedio >= 85:
    print(f"El promedio es mayor o igual a 85, el promedio es de {promedio}")
else:
    print(f"El promedio es menor que 85, el promedio es de {promedio}")

