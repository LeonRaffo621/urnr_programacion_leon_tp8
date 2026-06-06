"""Pida al usuario el nombre de 4 alumnos.
Valide que el nombre no esté vacío.
Guarde los nombres válidos en una lista.
Escriba los nombres en un archivo llamado alumnos.txt, un nombre por línea.
Cierre el archivo."""

lista_nombres=[]
while len(lista_nombres) < 4:
    nombre=str(input("nombre: "))
    chequeo=nombre.strip()
    if chequeo != "":
        lista_nombres.append(chequeo)
    else:
        print("entrada invalida, pruebe de nuevo ")

with open("alumnos.txt","w") as archivo:
    for i in lista_nombres:
        archivo.write(i + "\n")
