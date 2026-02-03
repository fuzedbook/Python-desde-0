#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("Semana_1//datos.csv")

#convertir a string toda una columna
df["edad"] = df["edad"].astype(str)

#mostrando el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))#

#reemplazando los datos "Fierros " por "Dominguez"
x = df["apellido"].replace("Fierros","Dominguez",inplace=True)

#eliminando filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#Creando un csv con el dataframe resultante (limpio)
df.to_csv("Semana_1//otros_datos.csv")