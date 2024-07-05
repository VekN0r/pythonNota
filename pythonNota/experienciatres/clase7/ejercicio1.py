import csv
import json
"""Construir programa que permita identificar las empresas que han tenido ventas inferiores a
$100.000.000, entre $100.000.001 y $200.000.000 y más de $200.000.000, a lo cual usted
deberá crear un archivo llamado “segmentacionEmpresas.json” que permita hacer esta dis-
tinción, a los datos listados más abajo deberá incorporar una columna adicional llamada
clasificacionEmpresa donde se indique “Pequeño Contribuyente”, “Mediano Contribuyente”
y “Gran Contribuyente”."""
def crear_csv(nombre_archivo, datos_csv):
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritorio_csv = csv.writer(archivo_csv)
        escritorio_csv.writerows(datos_csv)
def leer_csv(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return list(csv.reader(archivo))

datosLista = [
    ["rut", "nombre", "ventas"],
    ["72642413-6", "Comercial Calcetas Runner", 150000000],
    ["76437473-2", "Reparación Mac", 300000000],
    ["76254356-9", "ProgramaSoftware", 27500000],
    ["76077262-3", "Calzados Roma", 15000000],
    ["76310800-8", "Empresa Arcos", 80000000],
    ["76283690-4", "Casino Coffe", 120000000],
    ["76952985-5", "Cafe Express ltda", 50000000],
    ["76081440-2", "Vino Export SA", 20000000],
    ["76216579-1", "Cepa Merl LTDA", 30000000],
    ["76597875-0", "Comercial Ropa America", 60000000],
    ["76852106-3", "Empresas JP", 90000000],
    ["76887745-8", "Empresas ICata SA", 100000000],
    ["76210124-2", "Buses Peñalolen", 150000000],
    ["76802052-4", "Sandias Paine LTDA", 70000000],
    ["76575973-1", "Modas Junior P", 400000000],
    ["76869384-2", "Bar del 81", 25000000],
    ["76877803-6", "Empresas LLS", 8000000],
    ["76706124-0", "Empresas luz y vida SA", 3000000],
    ["76162938-1", "Empresa Matrix", 120000000]
]
crear_csv('listadoRutEmpresas.csv',datosLista)
datos_csv = leer_csv('listadoRutEmpresas.csv')
datosDict = []

for datos in datos_csv[1:]:
    ventas = int(datos[2])
    tipoContribuyente = ""
    if ventas >= 200000:
        tipoContribuyente = "Gran contribuyente"
    elif 100000 <= ventas < 200000:
        tipoContribuyente = "Medianoi contribuyente"
    else:
        tipoContribuyente = "Pequeño contribuyente"         
    diccionario = {
        "rut" : datos[0],
        "nombre" : datos[1],
        "ventas" : datos[2],
        "Contribuidor" : tipoContribuyente }
    datosDict.append(diccionario)
print(datosDict)        

for i in datosDict: #para corroborar si esta bien
    for clave, valor in i.items():
        print(f"{clave}:{valor}")
def crearJson(nombreArchivo, datos):
    with open(nombreArchivo, 'w') as archivo_json:
        json.dump(datos, archivo_json, indent=4)
    print(f"El archivo '{nombreArchivo}' se guardó correctamente")

crearJson("listaEmpresas.json", datosDict)