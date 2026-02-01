archivo = open("Semana_1//yo.txt")
#leer archivo completo
#archivo_leido = archivo.read()

#leer linea por linea 
#linea_1 = archivo.readlines()

#leer una sola linea
#linea = archivo.readline()

#cerrar el archivo 
#archivo.close

#print(linea)

#leer txt optimamente
#abriendo el archivo con with open
#with open("Semana_1//yo.txt", encoding="UTF-8") as archive:
    #leemos el archivo
   # contenido = archive.read()
    #mostrando el archivo
  #  print(contenido)
#no es necesario cerrar el archivo

with open("Semana_1//yo.txt",'w',encoding="UTF-8", ) as archive:
    #Sobre escribiendo el archivo
    #archive.write("Esto lo escribi desde el codigo")
    
    #agregando lineas con writelines \n importante
    #archive.writelines(["Yo que se \n","otra cosa"])
    archive.write("\n")
    for i in range(5):
        archive.write(f"Linea {i+1} agregada \n")