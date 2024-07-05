
"""Creen un programa que la lectura de un archivo CSV llamado 'datos.csv' que contiene
información sobre personas, incluyendo su nombre, edad y comuna. Para cada registro
en el archivo, se evalúa la edad y se determina si la persona es mayor o menor de edad.
La información, que incluye el nombre, la edad, el estado de edad y la comuna, se
imprime en la consola. Además, los registros de personas mayores o iguales a 25 años se
recopilan en una lista llamada mayores. La lista con usuarios mayores o iguales a 25 años
se guarda en un archivo JSON llamado 'mayores.json', se adjunta el conjunto de datos a
incorporar en datos.csv"""
import csv
import json
def crear_csv(nombre_archivo, datos_csv):
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(datos_csv)

datos_csv = [
    ["Nombre", "Edad", "Comuna"],
    ["Juan", "21", "Puente Alto"],
    ["María", "30", "Concepción"],
    ["Carlos", "22", "Viña Del Mar"],
    ["Estela", "25", "Puerto Mont"]
]        

print(datos_csv)
crear_csv("datos.csv", datos_csv)
mayoresEdad = []
with open("datos.csv","r") as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        edadUser = int(fila['Edad'])
        if edadUser >= 25:
            nombre = fila['Nombre']
            
            edad = int(fila['Edad'])
            comuna = fila['Comuna']
            estadoEdad = "Mayor de Edad"
            diccionario = {
                "Nombre" : nombre,
                "Edad" : edad,
                "Estado de edad" : estadoEdad,
                "Comuna"  : comuna
            }
            mayoresEdad.append(diccionario)    

for i in mayoresEdad:
    for clave, valor in i.items():
        print(clave,valor)

print("Personas mayores en formato JSON:")
def crearJson(nombreArchivo, datos):
    with open(nombreArchivo, 'w') as archivo_json:
        json.dump(datos, archivo_json, indent=4)
    print(f"El archivo '{nombreArchivo}' se guardó correctamente")
crearJson("MayoresEdad.json",mayoresEdad)                      