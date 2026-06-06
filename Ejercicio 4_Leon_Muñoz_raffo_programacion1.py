"""Se tiene un archivo llamado temperaturas.txt con el siguiente contenido:

Bariloche;12
Viedma;20
Roca;18
Bariloche;15
Escribí un programa que:

Lea el archivo línea por línea.
Separe cada línea usando split(";").
Genere un diccionario donde:
la clave sea la ciudad;
el valor sea una lista de temperaturas registradas.
Muestre el diccionario final."""
diccionario={}
with open("temperaturas.txt","r") as archivo:
    for i in archivo:
        lista=i.strip().split(";")
        ciudad=lista[0]
        temp=lista[1]
        if ciudad not in diccionario:
            diccionario[ciudad]=[]
        diccionario[ciudad].append(temp)  
print(diccionario)