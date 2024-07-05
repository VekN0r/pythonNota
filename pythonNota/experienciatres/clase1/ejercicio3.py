"""3) Cree una lista y comience a almacenar nombres, cada vez que se agregue un
nombre nuevo, el sistema preguntará si desea agregar otro nombre, deberá agregar
nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower()
y upper() )Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de
caracteres. ."""
nombres = []
nombreCorto = ""
while True:
    añadirNom = input("Ingrese nombre, para salir escriba No")
    if añadirNom.lower() == "no": 
        break
    nombres.append(añadirNom)
if nombres:
    nombreCorto = nombres[0]
    for nombreB in nombres:
        if len(nombreB) < len(nombreCorto):
            nombreCorto = nombreB
nombres.remove(nombreCorto)
print(f"El nombre más corto es {nombreCorto}")        