mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
    ]

tipos_mediciones=set()
final={}
for i in mediciones:
    lista=i
    lugar1=lista[2]
    medicion=lista[1]
    if lugar1 not in final:
        final[lugar1]=[]
    final[lugar1].append(medicion)

    if lista[0] not in tipos_mediciones:
        tipos_mediciones.add(lista[0])
print(tipos_mediciones)
print(final)
