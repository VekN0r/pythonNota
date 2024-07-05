import csv

def crear_csv(nombre_archivo, datos_csv):
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(datos_csv)

datos_csv = [
    ["Nombre", "Edad", "Comuna", "Estado de Edad"]
]

with open("datos.csv", "r") as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    filas_actualizadas = []
    for fila in lector_csv:
        nombre = fila['Nombre']
        edad = int(fila['Edad'])
        if edad >= 25:
            estado_edad = "Es mayor de edad"
        else:
            estado_edad = "Es menor de edad"
        comuna = fila['Comuna']
        fila['Estado de Edad'] = estado_edad
        filas_actualizadas.append(fila)
        print(f"Nombre: {nombre} Edad: {edad} Comuna: {comuna} Estado de Edad: {estado_edad}")

# Escribir las filas actualizadas en un nuevo archivo CSV
crear_csv("datos_actualizados.csv", filas_actualizadas)
