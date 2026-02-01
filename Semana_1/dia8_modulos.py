#importando un modulo y asignandole el nombre "m_saludar"
#importando dia8_ex_modulos as m_salduar

#desde ese modulo importamos dos funciones y les cambiamos el nombre
from Semana_1.dia8_ex_modulos import saludar as msaludo
import Semana_1.dia8_ex_modulos as saludo

#creamos las variables con el saludo

modulo_saludar = msaludo("Oscar")

print(modulo_saludar)

#para ver las propiedades y metodos del namespace
#print(dir(msaludo))

#accedemos al nombre del modulo
print(saludo.__name__)

#si el modulo estuviera en una carpeta en la misma ruta
#import dia8_ex_modulos.saludar as m_saludar
