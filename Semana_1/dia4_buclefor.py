animales = ["perro", "gato", "loro", "hamster"]
numeros = [10, 20 ,30 ,40, 50]

#Recorriendo la lista de animales
for animal in animales:
    print(f"El animal ahora es :{animal}")
    
#Recorriendo la lista de numeros
#for num in numeros:
   # print(num)
    
#Juntando listas
#for numero,animall in zip(animales,numeros):
    #print(numero)
    #print(animall)
    
#Haciendo una lista de numeros de tal. numero a tal nuemero
#for num in range(5,10):
   # print(num)
    
#Forma no optima de recorrer una lista con numero y valor
for num in range(len(numeros)):
    print(numeros[num])
    
#Forma correcta de recorred una lista con numero y valor
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es {indice} y el valor es {valor}")
    
#Usando en for else
for numero in numeros:
    print(f"valor actual {numero}")
else:
    print("Bucle terminado")
    
    
#Diccionario
diccionario = {
    "nombre" :"Oscar",
    "edad" : 17,
    "altura": 180
}

#Solo mostrar la clave
for clave in diccionario:
    print(clave)
    
#Mostrar clave y valor
for dict in diccionario.items():
    print(dict)
    
frutas = ["manzana", "pera", "uva", "durazno", "melon", "ciruela", "sandia"]

#Saltando un valor de la lista
#for fruta in frutas:
   # if fruta == "pera":
    #    continue
    #print(f"Me voy a comer una: {fruta}")
   
#Evitar que el bucle siga continuando  
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == "durazno":
        break

print("bucle terminado")

#Recorrer una cadena de texto
cadena = "Hola soy oscar"
numbers = [5,6,7,8]
for letra in cadena: 
     print(letra)
     
#for en una sola linea de codigo
numbers = [x*2 for x in numbers]
print(numbers)