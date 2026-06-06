def limpiar(texto):
    return texto.strip().capitalize()

def es_valido(nombre):
    if len(nombre) >= 3:
        return True
    return False

nombres = [" bart ", "ED", " walter", "rick "]
validos = []

for nombre in nombres:
    nombre_limpio = limpiar(nombre)

    if es_valido(nombre_limpio):
        validos.append(nombre_limpio)

print(validos)


"""Responder:

¿Qué hace el programa?
¿Qué hace la función limpiar?
¿Qué hace la función es_valido?
¿Qué nombres quedan almacenados en validos?
¿Qué imprime el programa al finalizar?

El programa consta de dos funciones, dos variables conformadas por listas, un bucle for, un 
condicional y un print. La funcion "limpiar" recibe un texto y devuelve el mismo texto eliminando
los espacios delanteros,finales y ademas pone la primera letra en mayuscula y el resto en minuscula.
La funcion "es_valido" recibe un nombre y evalua si la cantidad de letras del mismo es 3 o mayor, en
caso de que sea asi devuelve un true, en caso contrario devuelve un false.
Luego se nos definen la variable "nombres" la cual es una lista con 4 datos, y tambien la variable 
"validos" que es una lista vacia. Lo siguiente quehace el programa es en un bucle for crea una nueva
variable, "nombre_limpio" el cual llama a la funcion limpiar y le va dando los datos de la lista 
"nombres", luego evalua con un if a "nombre_limpio" con la funcion "es_valido", si resulta ser True
a la lista "validos" le agrega "nombre_limpio", en este caso los nombres que quedan almacenados son: 
Bart, Walter y Rick, ed no porque no cumple la condicion de "es_valido". Por ultimo el programa imprime
la lista de validos: ["Bart", "Walter", "Rick"]"""
