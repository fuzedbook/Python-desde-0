import csv

#with open("Semana_1//datos.csv") as datos:
    #reader = csv.reader(datos)
    #for row in reader:
    #    print(row)
        
#leer csv con pandas
import pandas as pd 
#usando la funcion read_csv para leer el archivo csv
df = pd.read_csv("Semana_1//datos.csv")
df2 = pd.read_csv("Semana_1//datos.csv")
#obteniendo los datos de la columna nombre
nombres = df["nombre"]
#Slicing
cadena = "0123456789"
#print(cadena[0:3])

#ordenando el dataframe por la edad
df_ordenado = df.sort_values("edad")

#ordenandolo de forma descendente
df_ordenadodesc = df.sort_values("edad", ascending=False)

#concatenando los dos data frames
df_concatenado = pd.concat([df, df2])

#accediendo a las primera fila con head()
primerFila = df.head(3)

#accediendo a las ultimas filas con tail()
ultimaFila = df.tail(2)

#accediendo a la cantidad de columnas y filas con shape
filas_totales,columnas_totales = df.shape

#Obteniendo datos estadisticos del df
df_info = df.describe()

#accediendo a un elemento especifico del df
elemento = df.loc[2, "edad"]

#accediendo a la edad de la fila 2 con iloc
ielemento = df.iloc[2,2]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a la columna 3 con loc
fila3 = df.loc[2, :]

#accediendo a filas con edad mayor que 30
mayor30 = df.loc[df["edad"]>30,:]
    

print(mayor30 )