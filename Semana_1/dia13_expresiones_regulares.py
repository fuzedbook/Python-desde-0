import re

texto = '''Hola, esta es la cadena 1 y es la linea numero 1
esta es la linea numero 2 del texto
Y esta es la linea final del texto de expresiones regulares'''

#Haciendo una busqueda simple
search = re.search("Hola",texto)
find = re.findall("esta",texto)

#\d - Busca digitos numericos del 0-9
digitos = re.findall(r"\d", texto)
#\D - Busca todo menos digitos numericos del 0-9
NoDigitos = re.findall(r"\D", texto)
#\w - Busca caracteres alfa numericos [a-z. A-Z 0-9 _]
alfanum = re.findall(r"\w", texto)
#\W - Busca todo menoscaracteres alfa numericos [a-z. A-Z 0-9 _]
Noalfanum = re.findall(r"\W", texto)
#\s - Busca espacios en blanco - espacios, tabs, saltos de linea
blanco = re.findall(r"\s", texto)
#\S - Busca todo menos espacios en blanco - espacios, tabs, saltos de linea
Noblanco = re.findall(r"\S", texto)
#Busca saltos en linea
SaltoLinea = re.findall(r"\n",texto)
#Busca todo menos saltos en linea
NosaltoLinea = re.findall(r"\.", texto)
#. - Cancelar caracteres especiales
Nocaracter = re.findall(r".", texto)
#\ - Cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
caracter = re.findall(r"\.", texto)

#armando una cadena que busque un numero seguido de un punto y un espacio

print(caracter)