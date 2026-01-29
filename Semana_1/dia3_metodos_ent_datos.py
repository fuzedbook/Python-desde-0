cadena1 = "Hola soy oscar"
cadena2 = "Bienvenido a python"

#convierte a mayuscula 
mayusc = cadena1.upper()
#convierte a minuscula
minusc = cadena1.lower()
#primera letra a mayuscula
primmayusc = cadena1.capitalize()

#Buscamos una cadena dentro de otra cadena, si no encuentra devuelve -1
busqueda_find = cadena1.find("h")
#buscamos una cadena en otra cadena, si no encuentra marca error
busqueda_index = cadena1.index("H")

#Si es numerico devuelve true, sino devuelve false - Puede revisar aunque sea dentro de un texto
es_numerico = cadena1.isnumeric()
#si es alfa numerico devuelve true, sino devuelve false - los espacios cuentan, solo letras de la A - Z
es_alfanumerico = cadena1.isalpha()

#En vez de encontrar una coincidencia, nos dice cuantas veces se encontro esa coincidencia, buscamos una cadena en otra cadena, 
contar_coincidencias = cadena1.count("a")
#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con una cadena dada, la cadena empieza con?
empieza_con = cadena1.startswith("Ho")
#Verificamos si una cadena termina con:
termina_con = cadena1.endswith("ar")

#remplaza un pedazo de la cadena dada por otra
cadena_nueva = cadena1.replace("la", "lu")
#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(" ")

#print(cadena_separada)


#Creando una lista con list()
lista = list(["hola", "Oscar", True, 90])
#print(lista)

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("JAJAJJAJA")
#agregando un elemento a la lista en un lugar especifico
lista.insert(2, "estw")
#agregando varios elementos a la lista
lista.extend([1,4,5,False])

#eliminando un elemento de la lista por su indice
lista.pop(9)#-1 para eliminar el ultimo
#removiendo un elemento de la lista por su valor, nombre, etc.
lista.remove("Oscar")
#remueve todos los elementos de la lista
#lista.clear()

#ordena los elementos de forma ascendente, solo numeros, los false van primero luego true luego numeros 
#lista.sort() #si usas adentro reverse=true se invierte
#invirtiendo los elementos de una lista
lista.reverse()


diccionario = {
    "nombre" : "Oscar",
    "edad" : 17,
    "altura" : 180
}

#Devuelve las claves
claves = diccionario.keys()
#devuelve el valor de una clave
valor_clave = diccionario.get("nombre")
#elimina todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre")
#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()


#INput()
#pedirle datos al usuario
nombre = input("Dime tu nombnre: ")

#pedirle numeros al usuario, lo convierto en entero y lo multiplico por 2
#numb = int(nombre) * 2

#convierte el numero a float, numero con decimal, con coma, con punto
numn_float = float(nombre) * 2

print(numn_float)