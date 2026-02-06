import re

texto = '''Hola, esta es 444 la cadena 1 y es la linea numero 1
esta es la linea numero 2 del texto
Y esta es la linea final del texto de expresiones regulares'''

#^ Busca el inicio de una linea
inicio = re.findall(r'^esta', texto,flags=re.M)
#$ Busca el final de una linea
final = re.findall(r'regulares$', texto)
#{n} busca n cantidad de veces el valor de la izquierda - 3 numeros juntos
valor = re.findall(r'\d{3}', texto, flags=re.M)
#{n,m} al menos n y como maximo m
minmax = re.findall(r'\d{1,3}', texto)
#| Busca una cosa o la otra
unaotra = re.findall(r'hola,| esta ',texto,flags=re.IGNORECASE)
print(unaotra)
